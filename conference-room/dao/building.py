from typing import Dict

class BuildingDAO:

    def __init__(self) -> None:
        self.building: Dict = dict()
    
    def setBuilding(self,building):
        self.building = building
    
    def getBuilding(self):
        return self.building