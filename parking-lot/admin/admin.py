from admin.account import Account
from admin.address import Address
from parking_lot.parking_floor import ParkingFloor
from parking_lot.parking_lot import ParkingLot
from parking_lot.parking_slot import ParkingSlot


class Admin(Account):
    def __init__(self, name: str, email: str, password: str, address: Address, empId: str) -> None:
        super().__init__(name, email, password, address, empId)

    def addParkingFloor(parkingLot: ParkingLot, parkingFloor: ParkingFloor) -> bool:
        pass
    
    def addParkingSlot(parkingFloor: ParkingFloor, parkingSlot: ParkingSlot) -> bool:
        pass
    
