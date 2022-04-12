from typing import Dict


class BuildingDAO:

    def __init__(self) -> None:
        self.building : Dict = dict()
    
    def getBuildingData(self):
        return self.building
    
    def setBuildingData(self,building):
        self.building = building