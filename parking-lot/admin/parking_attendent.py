from admin.account import Account
from admin.parking_ticket import ParkingTicket
from admin.payment import Payment
from admin.payment_info import PaymentInfo
from constants.enums import PaymentType
from parking_lot.vehicle import Vehicle


class ParkingAttendent(Account):
    def __init__(self, paymentService: Payment) -> None:
        pass

    def processVehicleEntry(Vehicle: Vehicle) -> bool:
        pass

    def processPayment(parkingTicket: ParkingTicket, paymentType: PaymentType) -> PaymentInfo:
        pass