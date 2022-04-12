from controllers.conference import ConferenceController


class Driver:

    def __init__(self):
        self.conferenceController = ConferenceController()

    def startServer(self):
        print("Enter Commands..!!")
        while True:
            command = input()
            splitCommand = command.split(" ")

            if "ADD BUILDING" in command:
                self.conferenceController.createBuilding(splitCommand[2])
            elif "ADD FLOOR" in command:
                self.conferenceController.createFloor(splitCommand[2],splitCommand[3])
            elif "ADD CONFERENCE" in command:
                self.conferenceController.createConference(splitCommand[2],splitCommand[3],splitCommand[4])
            elif "LIST BOOKING" in command:
                self.conferenceController.listAllBookedSlots(splitCommand[2],splitCommand[3])
            elif "BOOK" in command:
                self.conferenceController.bookConference(splitCommand[2],splitCommand[3],splitCommand[4],splitCommand[1])
            else:
                print("WRONG COMMAND")
                break

if __name__ == "__main__":
    driver = Driver()
    driver.startServer()