var droneHubBaseUrl = "https://localhost:5000/";
string currentJob = "";

// Generate guid
Guid guid = Guid.NewGuid();
Console.WriteLine($"Drone booting up: {guid}");

// Send ID to DroneHub
Post("drone/register/drone", guid.ToString());

while (true)
{
    if (currentJob == "")
    {
        currentJob = Get("job");
        Post("drone/updatestatus", "Starting");
    }
    else
    {
        Post("drone/updatestatus", "In Progress");
        Post("drone/updatepos", "{\"x\":2, \"y\":5)");
        Post("drone/camera", GenerateImageString());
    }

    Thread.Sleep(2000);
}

bool Post(string parameters, string payload)
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

string Get(string parameters)
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

string GenerateImageString()
{
    var bytes = File.ReadAllBytes("field.png");
    return Convert.ToBase64String(bytes);
}