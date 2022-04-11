from admin.parking_ticket import ParkingTicket
from admin.payment_info import PaymentInfo
from constants.enums import PaymentType


class Payment:
    def __init__(self) -> None:
        pass

    def makePayment(self, parkingTicket: ParkingTicket, paymentType: PaymentType ) -> PaymentInfo:
        pass