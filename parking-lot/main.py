from typing import List
from enums.enum import Vehicle
from gate.gate import Entrance, Exit
from parking_floors.parking_floor import ParkingFloor
from parking_lots.parking_lot import ParkingLot
from parking_slots.parking_slot import ParkingSlot

class Starter:

    def __init__(self) -> None:
        pass

    def start_app(self) -> None:

        while 1:

            print("1 ---> Add Parking Lot" )
            print("2 ---> Add Parking Floor" )
            print("3 ---> Add Parking Slot" )

            choice = int(input())
            if choice == 1:
                print('How many Parking Slot do you want on each floor ??')
                no_of_slots = int(input())

                slots: List[ParkingSlot]

                for i in range(no_of_slots):
                    slots.append( ParkingSlot(i+1,True,Vehicle.CAR,100,Vehicle.CAR))
                
                print('How many Parking Floor do you want ??')
                no_of_floor = int(input())

                floors: List[ParkingFloor]

                for i in range(no_of_floor):
                    floors.append( ParkingFloor(i+1,slots))
                
                print(ParkingLot(1,floors,"Jetpur",Entrance(1),Exit(1)).get_detail())
            
            elif choice == 2:
                
                print('Enter Parking Lot Id ??')
                lot_id = int(input())

                slots: List[ParkingSlot]

                for i in range(no_of_slots):
                    slots.append( ParkingSlot(i+1,True,Vehicle.CAR,100,Vehicle.CAR))
                
                print('How many Parking Floor do you want ??')
                no_of_floor = int(input())

                floors: List[ParkingFloor]

                for i in range(no_of_floor):
                    floors.append( ParkingFloor(i+1,slots))
                
                print(ParkingLot(1,floors,"Jetpur",Entrance(1),Exit(1)).get_detail())
                
                