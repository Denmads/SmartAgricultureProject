namespace ConsoleApp
{
    public class DroneHub
    {
        private readonly string droneHubBaseUrl = "https://localhost:5000/";

        public bool Post(string parameters, string payload)
        {
            try
            {
                using HttpClient client = new();
                client.BaseAddress = new Uri(droneHubBaseUrl);
                HttpResponseMessage response = client.PostAsync(parameters, new StringContent(payload)).Result;
                return response.IsSuccessStatusCode;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to reach {droneHubBaseUrl}: {ex.Message}");
                return false;
            }
        }

        public string Get(string parameters)
        {
            try
            {
                using HttpClient client = new();
                client.BaseAddress = new Uri(droneHubBaseUrl);
                HttpResponseMessage response = client.GetAsync(parameters).Result;
                if (response.IsSuccessStatusCode)
                {
                    return response.Content.ReadAsStringAsync().Result;
                }
                return "";
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to reach {droneHubBaseUrl}: {ex.Message}");
                return "";
            }
        }
    }
}
