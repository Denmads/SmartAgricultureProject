using System.Net.Http.Headers;

Console.WriteLine("Drone booting up test...");

HttpClient client = new HttpClient();
client.BaseAddress = new Uri("https://localhost:49159/");
client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
HttpResponseMessage response = client.GetAsync("position").Result;
if (response.IsSuccessStatusCode)
{
    var products = response.Content.ReadAsStringAsync().Result;
    Console.WriteLine($"{products}");
}
else
{
    Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
}