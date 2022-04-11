
from admin.parking_ticket import ParkingTicket
from admin.payment_info import PaymentInfo
from constants.enums import Vehicle


class Vehicle:
    def __init__(self, licenceNumber: str, vehicleType: Vehicle, parkingTicket: ParkingTicket, paymentInfo: PaymentInfo) -> None:
        pass