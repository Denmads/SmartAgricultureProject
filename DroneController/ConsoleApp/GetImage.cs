namespace ConsoleApp
{
    public static class GetImage
    {
        public static string GetBase64()
        {
            Random rnd = new();
            string path = $"Images/{ rnd.Next(11).ToString() }.png";
            var bytes = File.ReadAllBytes(path);
            return Convert.ToBase64String(bytes);
        }

    }
}
