from enums.enum import Vehicle


class ParkingSlot:
    
    def __init__(self, slotId: int, isFree: bool, vehicle: Vehicle, costPerHour: float, parkingSpaceType: Vehicle) -> None:
        self.slotId = slotId
        self.isFree= isFree
        self.vehicle = vehicle
        self.costPerHour = costPerHour
        self.parkingSpaceType = parkingSpaceType
        