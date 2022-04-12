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
    def validateConferenceRoom(buildingData,buildingName,floorName,conferenceRoomName):
        if conferenceRoomName in buildingData[buildingName][floorName]:
            return True
        return False
    
    @staticmethod
    def validateTimeSlot(existingTimeSlot,timeSlot):
        existingTimeSlotClone = existingTimeSlot.copy()

        if len(existingTimeSlotClone) < 1:
            return True
        
        if int(timeSlot[0]) >= int(timeSlot[1]):
            print("Start time can't be greater than or equal to end time.")
            return False
        
        if abs(int(timeSlot[0]) - int(timeSlot[1])) >= 12:
            print("We can't book more than 12 hours")
            return False

        slot = [int(timeSlot[0]),int(timeSlot[1])]

        existingTimeSlotClone.append(slot)

        existingTimeSlotClone.sort(key = lambda x : x[0])

        for slotIndex in range(1,len(existingTimeSlotClone)):
            if existingTimeSlotClone[slotIndex][0] < existingTimeSlotClone[slotIndex-1][1]:
                print("Overlapping Time Slots Found with given time slot..!!!")
                return False
        return True
    
    @staticmethod
    def cancelTimeSlot(existingTimeSlot,timeSlot):
        existingTimeSlotClone = existingTimeSlot.copy()

        if len(existingTimeSlotClone) < 1:
            print("Can't perform cancel action.")
            return False
        
        return True