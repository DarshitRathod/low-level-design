from enum import Enum

class Vehicle(Enum):
    CAR = 1,
    BIKE = 2,
    TRUCK = 3

class PaymentType(Enum):
    CASH = 1,
    UPI = 2,
    DEBIT_CARD = 3,
    CREDIT_CARD = 4

class ParkingTicketStauts(Enum):
    PAID= 1,
    UNPAID = 2

class PaymentStatus(Enum):
    UNPAID = 1, 
    PENDING = 2, 
    COMPLETED = 3, 
    DECLINED = 4, 
    CANCELLED = 5, 
    REFUNDED = 6