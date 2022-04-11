from typing import List
from admin.address import Address
from admin.parking_attendent import ParkingAttendent
from constants.enums import Vehicle
from parking_lot.gate import Gate
from parking_lot.parking_floor import ParkingFloor

class ParkingLot:

    def __init__(self, parkingFloors: List[ParkingFloor], entrance: Gate, exit: Gate, address: Address, parkingLotName: str) -> None:
        pass

    def isParkingSpaceAvailableForVehicle(self,vehicle: Vehicle) -> bool:
        pass
    
    def updateParkingAttendent(self, parkingAttendent: ParkingAttendent, getId: int) -> bool:
        pass