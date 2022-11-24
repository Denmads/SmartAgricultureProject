from typing import Union
import requests as req
import os
from util import MovePoint, DroneStatus

class BackendAPI:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def _url(self, endpoint: str):
        return os.path.join(self.base_url, endpoint)
    
    def register_drone(self, id: str) -> int:
        try:
            r: req.Response = req.post(self._url("drone/register/drone"), json={"id": id})
            return r.status_code
        except:
            return 999
    
    def check_for_job(self, id: str) -> Union[MovePoint, None]:
        try:
            r: req.Response = req.post(self._url("drone/job"), json={"id": id})
            if r.status_code != 200:
                return None
            else:
                content: dict = r.json()
                
                if not content["hasJob"]:
                    return None
                
                return MovePoint(content["x"], content["y"], 2)
        except:
            return None

    def update_status(self, id: str, status: DroneStatus) -> int:
        try:
            r: req.Response = req.get(self._url("drone/updatestatus"), params={"id": id, "status": status.value})
            return r.status_code
        except:
            return 999
    
    def update_position(self, id: str, x: float, y: float) -> int:
        try:
            r: req.Response = req.get(self._url("drone/updatepos"), params={"id": id, "x": round(x), "y": round(y)})
            return r.status_code
        except:
            return 999
        
    def update_camera(self, id: str, img: str) -> bool:
        """Return wether or not it should harvest. True for harvest"""
        try:
            r: req.Response = req.post(self._url("drone/camera"), json={"id": id, "image": img})
            
            if r.status_code != 200:
                return False
            else:
                return r.json()["harvest"]
            
        except:
            return False