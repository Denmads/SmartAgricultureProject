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
    Console.WriteLine($"Drone registered: {droneData.drone_id}");
}

while (true)
{
    if (currentJob != null && currentJob.hasJob)
    {
        FlyDrone();

        var json = Jsonfy(droneData.position);
        Console.WriteLine(json);
        droneHub.Post("drone/updatepos", json);

        if (DestinationReached(droneData.position, currentJob))
        {
            Console.WriteLine("Destination reached");
            currentJob = new();

            // Sending image
            var image = ConsoleApp.GetImage.GetBase64();
            Console.WriteLine(image.Substring(0, 100));
            //droneHub.Post("drone/camera", GenerateImageString());

            Thread.Sleep(5000);
        }

    }
    else
    {
        currentJob = droneHub.GetNewJob();
        var jobJson = JsonConvert.SerializeObject(currentJob, Formatting.Indented);
        Console.WriteLine($"Update status {jobJson}");
        droneHub.Post("drone/updatestatus", "{\"drone_id\": " + $"\"{droneData.drone_id}\", \"status\": \"working\" }}");
        ;
    }

    Thread.Sleep(500);
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