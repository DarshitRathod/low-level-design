from dao.building import BuildingDAO
from validator.validate import Validate


class Conference:

    def __init__(self) -> None:
        self.buildingData = BuildingDAO().getBuildingData()

    def addBuilding(self,buildingName):

        if Validate.validateBuilding(self.buildingData,buildingName):
            print("{name} building is already present...!!".format(name=buildingName))
            return

        self.buildingData[buildingName] = {}
        print("{name} building has been added...!!".format(name=buildingName))
    
    def addFloor(self,buildingName,floorName):

        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("{name} building is not present...!!".format(name=buildingName))
            return
        
        if Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("{name} floor is already present...!!".format(name=floorName))
            return

        floor = {}
        floor[floorName] = {}
        self.buildingData[buildingName] = floor
        print("{name} floor has been added...!!".format(name=floorName))
    
    def addConferenceRoom(self,buildingName,floorName,conferenceRoomName):

        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("{name} building is not present...!!".format(name=buildingName))
            return
        
        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("{name} floor is not present...!!".format(name=floorName))
            return
        
        if Validate.validateConferenceRoom(self.buildingData,buildingName,floorName,conferenceRoomName):
            print("{name} room is already present...!!".format(name=conferenceRoomName))
            return

        conferenceRoom = {}
        conferenceRoom[conferenceRoomName] = []
        self.buildingData[buildingName][floorName] = conferenceRoom
        print("{name} conference room has been added...!!".format(name=conferenceRoomName))

    def bookConferenceRoom(self,buildingName,floorName,conferenceRoomName,timeSlot):
        
        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("{name} building is not present...!!".format(name=buildingName))
            return
        
        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("{name} floor is not present...!!".format(name=floorName))
            return
        
        if not Validate.validateConferenceRoom(self.buildingData,buildingName,floorName,conferenceRoomName):
            print("{name} room is not present...!!".format(name=conferenceRoomName))
            return
        
        if not Validate.validateTimeSlot(self.buildingData[buildingName][floorName][conferenceRoomName], timeSlot.split(":")):
            return

        slot = timeSlot.split(":")
        self.buildingData[buildingName][floorName][conferenceRoomName].append([ int(slot[0]), int(slot[1])  ])
        print("Given time slot has been added..!!")
    
    def listBookedTimeSlots(self,buildingName,floorName):
        
        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("{name} building is not present...!!".format(name=buildingName))
            return
        
        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("{name} floor is not present...!!".format(name=floorName))
            return

        allRoomEmpty = True

        for room in self.buildingData[buildingName][floorName]:
            if len(self.buildingData[buildingName][floorName][room]) > 0:
                allRoomEmpty = False
        
        if allRoomEmpty:
            print("All Rooms for given floor and building are empty..!!")
            return
        
        for room in self.buildingData[buildingName][floorName]:
            for slot in self.buildingData[buildingName][floorName][room]:
                print(str(slot[0]) + ":" + str(slot[1]) + " " + str(floorName) + " " + str(buildingName) + " " + str(room))

    def cancelBookedTimeSlot(self,buildingName,floorName,conferenceRoomName,timeSlot):
        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("{name} building is not present...!!".format(name=buildingName))
            return
        
        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("{name} floor is not present...!!".format(name=floorName))
            return
        
        if not Validate.validateConferenceRoom(self.buildingData,buildingName,floorName,conferenceRoomName):
            print("{name} room is not present...!!".format(name=conferenceRoomName))
            return
        
        if not Validate.cancelTimeSlot(self.buildingData[buildingName][floorName][conferenceRoomName], timeSlot.split(":")):
            return

        slot = timeSlot.split(":")
        for slotIndex in range(len(self.buildingData[buildingName][floorName][conferenceRoomName])):
            if self.buildingData[buildingName][floorName][conferenceRoomName][slotIndex][0] == int(slot[0]) and self.buildingData[buildingName][floorName][conferenceRoomName][slotIndex][1] == int(slot[1]):
                self.buildingData[buildingName][floorName][conferenceRoomName].pop(slotIndex)
                break
        
        print("Given time slot has been removed..!!")