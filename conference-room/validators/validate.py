class Validate:

    def __init__(self) -> None:
        pass

    @staticmethod
    def validateBuilding(buildingData,buildingName):
        if buildingName in buildingData:
            return True
        return False

    @staticmethod
    def validateFloor(buildingData,buildingName,floorName):
        if floorName in buildingData[buildingName]:
            return True
        return False

    @staticmethod
    def validateRoom(buildingData,buildingName,floorName, conferenceRoom):
        if conferenceRoom in buildingData[buildingName][floorName]:
            return True
        return False

    @staticmethod
    def validateTimeSlot(existingTimeSlot, timeSlot):

        existingTimeSlotClone = existingTimeSlot.copy()

        if len(existingTimeSlotClone) < 1:
            return True
        
        if int(timeSlot[0]) >= int(timeSlot[1]):
            print("Start time can't be same or greater than end time")
            return False

        if abs(int(timeSlot[0]) - int(timeSlot[1])) >= 12:
            print("Duration can't be greater than 12 hours")
            return False
        
        slot = [int(timeSlot[0]), int(timeSlot[1])]

        existingTimeSlotClone.append(slot)
        existingTimeSlotClone.sort(key = lambda x: x[0])

        for i in range(1,len(existingTimeSlotClone)):
            if existingTimeSlotClone[i][0] < existingTimeSlotClone[i-1][1]:
                print("Overlapping Slots Found")
                return False