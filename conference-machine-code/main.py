from controller.conference import Conference


class Driver:

    def __init__(self) -> None:
        self.buildingController = Conference()
    

    def startServer(self):

        print("Start Entering Commands")
        
        while True:
            command = input()
            spitedCommand = command.split(" ")
            try:
                if "ADD BUILDING" in command:
                    self.buildingController.addBuilding(spitedCommand[2])
                elif "ADD FLOOR" in command:
                    self.buildingController.addFloor(spitedCommand[2],spitedCommand[3])
                elif "ADD CONFROOM" in command:
                    self.buildingController.addConferenceRoom(spitedCommand[2],spitedCommand[3],spitedCommand[4])
                elif "LIST BOOKING" in command:
                    self.buildingController.listBookedTimeSlots(spitedCommand[2],spitedCommand[3])
                elif "BOOK" in command:
                    self.buildingController.bookConferenceRoom(spitedCommand[2],spitedCommand[3],spitedCommand[4],spitedCommand[1])
                elif "CANCEL" in command:
                    self.buildingController.cancelBookedTimeSlot(spitedCommand[2],spitedCommand[3],spitedCommand[4],spitedCommand[1])
                else:
                    print("Wrong Command")
                    break
            except:
                print("Server Error..!!")

if __name__ == "__main__":
    driver = Driver()
    driver.startServer()