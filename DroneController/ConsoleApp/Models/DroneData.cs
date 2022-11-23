namespace ConsoleApp.Models
{
    public class DroneData
    {
        public string drone_id { get; set; } = "";
        public string status { get; set; } = "";
        public Position position { get; set; } = new();
    }
}
