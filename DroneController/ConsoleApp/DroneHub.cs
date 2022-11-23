using ConsoleApp.Models;
using Newtonsoft.Json;

namespace ConsoleApp
{
    public class DroneHub
    {
        private readonly string droneHubBaseUrl = "http://localhost:3000/";

        public Job GetNewJob()
        {
            var job = Get("job");

            if (job == null)
            {
                Random rnd = new();
                return new Job() { hasJob = true, X = rnd.Next(30), Y = rnd.Next(30) };
            }

            return (Job)JsonConvert.DeserializeObject(job);
        }

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

        public string? Get(string parameters)
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
                return null;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to reach {droneHubBaseUrl}: {ex.Message}");
                return null;
            }
        }
    }
}
