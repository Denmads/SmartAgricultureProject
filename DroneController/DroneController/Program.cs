var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapGet("api/position", () =>
{
    var position = DroneController.CurrentPosition.Get();
    position.UniqueId = builder.Configuration.GetValue<string>("UniqueId");
    return position;
})
.WithName("GetPosition");

app.MapGet("api/image", () =>
{
    return DroneController.GetImage.GetBase64();
})
.WithName("GetImage");

app.MapGet("api/imageRaw", () =>
{
    return DroneController.GetImage.GetRaw();
})
.WithName("GetImageRaw");

app.MapGet("api/job", () =>
{
    return @"Current job";
})
.WithName("GetJob");

app.MapPost("api/job", (string job) =>
{
    return $"retrieved {job}";
})
.WithName("PostJob");

app.Run();
