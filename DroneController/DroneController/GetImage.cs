namespace DroneController
{
    public static class GetImage
    {
        private static string Path => @"field.png";

        public static string GetBase64()
        {
            Byte[] bytes = File.ReadAllBytes(Path);
            return Convert.ToBase64String(bytes);
        }

        public static IResult GetRaw()
        {
            var mimeType = "image/png";
            FileInfo f = new FileInfo(Path);
            return Results.File(f.FullName, contentType: mimeType);
        }

    }
}
