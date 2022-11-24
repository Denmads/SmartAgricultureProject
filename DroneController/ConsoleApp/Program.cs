using ConsoleApp;
using ConsoleApp.Models;
using Newtonsoft.Json;

Job currentJob = new();

DroneData droneData = DroneInit.InitilizeDrone();
Console.WriteLine($"Drone booting up ...");

DroneHub droneHub = new();

// Send ID to DroneHub
while (true)
{
    Console.WriteLine($"Trying to register ({droneData.drone_id})...");
    bool registered = droneHub.Post("drone/register/drone", Jsonfy(droneData.drone_id));
    if (registered)
    {
        Console.WriteLine($"Drone registered: {droneData.drone_id}");
        break;
    }

    Console.WriteLine($"Error while registering, retrying in 5 seconds...");
    Thread.Sleep(5000);
}

droneData.status = "waiting";
droneHub.Post("drone/updatestatus", Jsonfy(droneData));
Console.WriteLine($"Drone status: {droneData.status}");

while (true)
{
    if (currentJob != null && currentJob.hasJob)
    {
        FlyDrone();

        var json = Jsonfy(droneData.position);
        Console.WriteLine($"New Position: {json}");
        droneHub.Post("drone/updatepos", json);
        Console.WriteLine($"drone/updatepos {json}");

        if (DestinationReached(droneData.position, currentJob))
        {
            Console.WriteLine("Destination reached");

            droneData.status = "done";
            var status = Jsonfy(droneData);
            droneHub.Post("drone/updatestatus", status);
            Console.WriteLine($"drone/updatestatus {status}");

            // Sending image
            var cameraImage = GetImage.GetImageObject();
            Console.WriteLine($"drone/camera: {cameraImage.image.Substring(0, 100)}");
            var image = Jsonfy(cameraImage);
            var result = droneHub.PostWithResult("drone/camera", image);

            var harvest = JsonConvert.DeserializeObject<Harvest>(result);
            if (harvest.harvest)
            {
                droneData.status = "harvest";
                droneHub.Post("drone/updatestatus", Jsonfy(droneData));
                for (int i = 0; i < 10; i++)
                {
                    Console.WriteLine($"{Jsonfy(droneData)}");
                    }
            }

            currentJob.hasJob = false;
        }
    }
    else
    {
        currentJob = droneHub.GetNewJob(Jsonfy(droneData.drone_id));
        if (currentJob != null)
        {
            droneData.status = "working";
            droneHub.Post("drone/updatestatus", Jsonfy(droneData));
            Console.WriteLine($"Drone status: {droneData.status}");
        }
    }

    Thread.Sleep(1000);
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