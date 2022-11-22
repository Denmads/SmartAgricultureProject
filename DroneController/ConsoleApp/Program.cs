using ConsoleApp.Models;
using Newtonsoft.Json;

Job currentJob = new() { hasJob = false, X = 0, Y = 0 };

// Generate guid
Guid guid = Guid.NewGuid();
Console.WriteLine($"Drone booting up: {guid}");

Position pos = new Position() { X = 0, Y = 0 };
var droneHub = new ConsoleApp.DroneHub();

// Send ID to DroneHub
droneHub.Post("drone/register/drone", guid.ToString());

while (true)
{
    if (currentJob.hasJob)
    {
        droneHub.Post("drone/updatestatus", "In Progress");
        droneHub.Post("drone/updatepos", JsonConvert.SerializeObject(pos, Formatting.Indented));
        droneHub.Post("drone/camera", GenerateImageString());
    }
    else
    {
        currentJob = (Job)JsonConvert.DeserializeObject(droneHub.Get("job"));
        droneHub.Post("drone/updatestatus", "Starting");
    }

    Thread.Sleep(2000);
}

string GenerateImageString()
{
    var bytes = File.ReadAllBytes("field.png");
    return Convert.ToBase64String(bytes);
}
