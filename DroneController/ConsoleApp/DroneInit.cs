using ConsoleApp.Models;

namespace ConsoleApp
{
    public class DroneInit
    {
        public static DroneData InitilizeDrone()
        {
            Random rnd = new();
            return new DroneData() 
            {
                drone_id = Guid.NewGuid().ToString(),
                status = "waiting",
                X = rnd.Next(30),
                Y = rnd.Next(30)
            };
        }

    }
}
