import random
from backendapi import BackendAPI
from time import sleep
import time
from util import DroneStatus

TIME_BETWEEN_MOVE_UPDATES = 1
TIME_BETWEEN_CAMERA_UPDATES = 5

class DroneController:
    
    def __init__(self, id: str, backend: BackendAPI, images: list[str]):
        self.id = id
        self.backend = backend
        self.images = images
        
        self.x: float = -1
        self.y: float = -1
        self.status: DroneStatus = DroneStatus.OFF
        
        self.job = None
        
        self.last_pos_update = None
        self.last_camera_update = None
        self.harvest_end_time = 0
        
    def boot(self):
        print("Drone booting...")
        self.status = DroneStatus.BOOTING
        self._ensure_registration()
        
        self.last_pos_update = int(time.time_ns() / 1000000)
        self.last_camera_update = int(time.time_ns() / 1000000)
        
        # Run lifecycle
        while True:
            if self.job is None or self.job.reached_point(self.x, self.y):
                self._check_for_job()
            
            if self.status == DroneStatus.HARVESTING:
                if time.time_ns() > self.harvest_end_time:
                    self._set_status(DroneStatus.WORKING)
                    print("Harvest done")
            else:
                time_diff_pos = self.last_pos_update - int(time.time_ns() / 1000000)
                if time_diff_pos >= TIME_BETWEEN_MOVE_UPDATES:
                    self._add_to_position(
                        self.job.get_x_move(TIME_BETWEEN_MOVE_UPDATES * 1000, self.x),
                        self.job.get_y_move(TIME_BETWEEN_MOVE_UPDATES * 1000, self.y)
                    )
                    print(f"New position: {self.x}, {self.y}")
                    
                time_diff_camera = self.last_camera_update - int(time.time_ns() / 1000000)
                if time_diff_camera >= TIME_BETWEEN_CAMERA_UPDATES:
                    self._send_image()
                
                
    
    def _ensure_registration(self):
        while True:
            print(f"Trying to register with id: {self.id}")
            status: int = self.backend.register_drone(self.id)
            
            if status == 200:
                return
            else:
                print("Failed to register. Retrying in 5 seconds...")
                sleep(5)
                
    def _check_for_job(self):
        print("checking for job...")
        response = self.backend.check_for_job(self.id)
        if response is None:
            print(f"No job available")
            self._set_status(DroneStatus.IDLE)
            self._print_status()
        else:
            self.job = response
            print(f"Got new job: {self.job.x}, {self.job.y}")
            self._set_status(DroneStatus.WORKING)
            self._print_status()
            
            if self.status == DroneStatus.IDLE:
                self._set_position(self.job.x, self.job.y)
    
    def _send_image(self):
        print("Sending camera feed. Awaiting response...")
        img = random.choice(self.images)
        should_harvest = self.backend.update_camera(self.id, img)
        
        if should_harvest:
            print("Starting harvest")
            self._set_status(DroneStatus.HARVESTING)
            self.harvest_end_time = int(time.time_ns() / 1000000) + random.randint(5000, 10000)
            
    
    def _set_position(self, x: float, y: float):
        self.x = x
        self.y = y
        self.backend.update_position(self.id, x, y)
        
    def _add_to_position(self, x: float, y: float):
        self.x += x
        self.y += y
        self.backend.update_position(self.id, self.x, self.y)
    
    def _set_status(self, status: DroneStatus):
        self.status = status
        self.backend.update_status(self.id, status)
                
    def _print_status(self):
        print(f"Status: {self.status._name_}")