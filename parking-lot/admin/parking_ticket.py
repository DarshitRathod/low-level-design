from datetime import date
from constants.enums import ParkingTicketStauts, Vehicle

class ParkingTicket:
    def __init__(self, ticket_id: int, levelId: int,slotId: int, vehicleEntryDateTime: date, vehicleExitDateTime: date, parkingSpaceType: Vehicle, totalCoast: float, parkingTicketStatus: ParkingTicketStauts ) -> None:
        pass 

    def updateTotalCoast() -> None:
        pass
    
    def updateVehicleExitTime() -> None:
        pass