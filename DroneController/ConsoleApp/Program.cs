using ConsoleApp;
using ConsoleApp.Models;
using Newtonsoft.Json;

Job currentJob = new();

DroneData droneData = DroneInit.InitilizeDrone();
Console.WriteLine($"Drone booting up ...");

DroneHub droneHub = new();

// Send ID to DroneHub
if (droneHub.Post("drone/register/drone", Jsonfy(droneData.drone_id)))
{
    Console.WriteLine($"drone/register/drone {Jsonfy(droneData.drone_id)}");
}

while (true)
{
    if (currentJob != null && currentJob.hasJob)
    {
        FlyDrone();

        var json = Jsonfy(droneData.position);
        droneHub.Post("drone/updatepos", json);
        Console.WriteLine($"drone/updatepos {json}");

        if (DestinationReached(droneData.position, currentJob))
        {
            droneData.status = "done";
            var status = Jsonfy(droneData);
            droneHub.Post("drone/updatestatus", status);
            Console.WriteLine($"drone/updatestatus {status}");

            // Sending image
            var cameraImage = GetImage.GetImageObject();
            Console.WriteLine($"drone/camera: {cameraImage.image.Substring(0, 100)}");
            var i = Jsonfy(cameraImage);
            droneHub.Post("drone/camera", i);

            currentJob = new();
            Thread.Sleep(5000);
        }
    }
    else
    {
        currentJob = droneHub.GetNewJob(Jsonfy(droneData.drone_id));
        droneData.status = "working";
        droneHub.Post("drone/updatestatus", Jsonfy(droneData));
        Console.WriteLine($"drone/updatestatus {Jsonfy(droneData)}");
    }

    Thread.Sleep(100);
}

void FlyDrone()
{
    if (droneData.position.X != currentJob.X)
    {
        droneData.position.X = currentJob.X > droneData.position.X ? droneData.position.X + 1 : droneData.position.X - 1;
    }

    if (droneData.position.Y != currentJob.Y)
    {
        droneData.position.Y = currentJob.Y > droneData.position.Y ? droneData.position.Y + 1 : droneData.position.Y - 1;
    }
}

bool DestinationReached(Position pos1, Position pos2)
{
    return pos1.X.Equals(pos2.X) && pos1.Y.Equals(pos2.Y);
}

string Jsonfy(object model)
{
    return JsonConvert.SerializeObject(model);
}