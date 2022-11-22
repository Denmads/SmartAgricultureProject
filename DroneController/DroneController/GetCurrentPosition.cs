using DroneController.Models;

namespace DroneController
{
    public static class CurrentPosition
    {
        private static Position Position { get; set; } = new Position(0, 0);

        public static Position Get()
        {
            Random r = new Random();

            Position.Latitude = (decimal)r.Next(5534344, 5534555) / 100000;
            Position.Longitude = (decimal)r.Next(1044524, 1045163) / 100000;

            return Position;

        }
    }
}
