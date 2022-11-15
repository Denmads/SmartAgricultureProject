from hub import Hub

if __name__ == "__main__":
    hub = Hub(name="test")
    
    print(hub.getName())

    print(hub.getAllDrones())

    for field in hub.fields:
        print(field.to_json())
    
    for drone in hub.drones:
        print(drone.to_json())