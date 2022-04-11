from datetime import date
from constants.enums import ParkingTicketStauts
from parking_ticket import ParkingTicket

class PaymentInfo:
    def __init__(self,amount: float, paymentDate: date, transactionId: int, parkingTicket: ParkingTicket, parkingTicketStatus: ParkingTicketStauts) -> None:
        pass    