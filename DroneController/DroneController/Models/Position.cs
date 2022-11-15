namespace DroneController.Models
{
    public class Position
    {
        public Position(decimal latitude, decimal longitude)
        {
            Latitude = latitude;
            Longitude = longitude;
        }

        public decimal Latitude { get; set; }
        public decimal Longitude { get; set; }
        public string UniqueId { get; set; }
    }
}
