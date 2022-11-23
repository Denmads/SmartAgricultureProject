namespace ConsoleApp
{
    public static class GetImage
    {
        public static CameraImage GetImageObject()
        {
            Random rnd = new();
            string path = $"Images/{ rnd.Next(11).ToString() }.png";
            var bytes = File.ReadAllBytes(path);
            CameraImage value = new() { image = Convert.ToBase64String(bytes) };
            return value;
        }
    }

    public class CameraImage
    {
        public string image { get; set; }
    }
}
