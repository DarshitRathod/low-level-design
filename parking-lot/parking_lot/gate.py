from admin.parking_attendent import ParkingAttendent
from admin.parking_ticket import ParkingTicket
from constants.enums import PaymentType, Vehicle


class Gate:
    def __init__(self, parkingAttendent: ParkingAttendent, gateId: int) -> None:
        pass

class Entrance(Gate):

    def __init__(self, parkingAttendent: ParkingAttendent, gateId: int) -> None:
        super().__init__(parkingAttendent, gateId)
    
    def getparkingTicket(vehicle :Vehicle) -> ParkingTicket:
        pass

class Exit(Gate):

    def __init__(self, parkingAttendent: ParkingAttendent, gateId: int) -> None:
        super().__init__(parkingAttendent, gateId)
    
    def payForParking(parkingTicket: ParkingTicket, payment_type: PaymentType):
        pass
