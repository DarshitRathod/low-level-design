from typing import List
from gate.gate import Gate
from parking_floors.parking_floor import ParkingFloor


class ParkingLot:
    
    def __init__(self, parking_lot_id: int, parking_floor: List[ParkingFloor], address: str, entrance: Gate, exit: Gate ) -> None:
        self.parking_lot_id = parking_lot_id
        self.parking_floor = parking_floor
        self.address = address
        self.entrance = entrance
        self.exit = exit

    def get_detail(self):
        return str(self.parking_floor) + " " + str(self.address) 
