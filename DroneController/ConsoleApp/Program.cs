using ConsoleApp.Models;
using Newtonsoft.Json;

Job currentJob = new();

// Generate guid
Guid guid = Guid.NewGuid();
Console.WriteLine($"Drone booting up: {guid}");

Position currentPosition = new() { X = 0, Y = 0 };
var droneHub = new ConsoleApp.DroneHub();

// Send ID to DroneHub
//droneHub.Post("drone/register/drone", guid.ToString());

while (true)
{
    if (currentJob != null && currentJob.hasJob)
    {
        FlyDrone();

        var json = JsonConvert.SerializeObject(currentPosition, Formatting.Indented);
        Console.WriteLine(json);
        //droneHub.Post("drone/updatepos", );

        if (DestinationReached(currentPosition, currentJob))
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
        var s = JsonConvert.SerializeObject(currentJob, Formatting.Indented);
        Console.WriteLine($"Starting flying towards {s}");
        //droneHub.Post("drone/updatestatus", "In Progress");
        //droneHub.Post("drone/updatestatus", $"Starting flying towards {s}");
        ;
    }

    Thread.Sleep(500);
}

void FlyDrone()
{

    if (currentPosition.X != currentJob.X)
    {
        currentPosition.X = currentJob.X > currentPosition.X ? currentPosition.X + 1 : currentPosition.X - 1;
    }

    if (currentPosition.Y != currentJob.Y)
    {
        currentPosition.Y = currentJob.Y > currentPosition.Y ? currentPosition.Y + 1 : currentPosition.Y - 1;
    }
}

bool DestinationReached(Position pos1, Position pos2)
{
    return pos1.X.Equals(pos2.X) && pos1.Y.Equals(pos2.Y);
}