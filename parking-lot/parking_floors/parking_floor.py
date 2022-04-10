from typing import List
from parking_slots.parking_slot import ParkingSlot


class ParkingFloor:
    def __init__(self, level_id: int, slots: List[ParkingSlot]) -> None:
        self.level_id = level_id
        self.slots = slots