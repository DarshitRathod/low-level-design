from dao.building import BuildingDAO
from validators.validate import Validate


class ConferenceController:

    def __init__(self) -> None:
        self.buildingData = BuildingDAO().getBuilding()
    
    def createBuilding(self,buildingName):
        
        if Validate.validateBuilding(self.buildingData,buildingName):
            print("Building Already Present...!!") 
            return
        
        self.buildingData[buildingName] = {}
        print(" Added building {Name} into the system.".format(Name = buildingName ))
    
    def createFloor(self,buildingName,floorName):

        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("Building Not Present...!!") 
            return

        if Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("Floor Already Present...!!") 
            return
        
        floor = {}
        floor[floorName] = {}
        self.buildingData[buildingName] = floor
        print(" Added floor {Name} into the system.".format(Name = floorName ))

    def createConference(self,buildingName,floorName, conferenceRoom):

        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("Building Not Present...!!") 
            return

        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("Floor Not Present...!!") 
            return
        
        if Validate.validateRoom(self.buildingData,buildingName,floorName, conferenceRoom):
            print("Conference Room already Present...!!") 
            return
        
        confRoom = {}
        confRoom[conferenceRoom] = []
        self.buildingData[buildingName][floorName] = confRoom
        print("Added Conference Room {Name} into the system.".format(Name = conferenceRoom ))
    
    def bookConference(self,buildingName,floorName, conferenceRoom, timeSlot):

        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("Building Not Present...!!") 
            return

        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("Floor Not Present...!!") 
            return
        
        if not Validate.validateRoom(self.buildingData,buildingName,floorName, conferenceRoom):
            print("Conference Room Not Present...!!") 
            return
        
        if not Validate.validateTimeSlot(self.buildingData[buildingName][floorName][conferenceRoom], timeSlot.split(":")):
            return
        
        slot = timeSlot.split(":")
        self.buildingData[buildingName][floorName][conferenceRoom].append([int(slot[0]), int(slot[1])])
        print("Added Slot into System")

    def listAllBookedSlots(self,buildingName,floorName):

        if not Validate.validateBuilding(self.buildingData,buildingName):
            print("Building Not Present...!!") 
            return

        if not Validate.validateFloor(self.buildingData,buildingName,floorName):
            print("Floor Not Present...!!") 
            return

        allRoomEmpty = True
        for room in self.buildingData[buildingName][floorName]:
            if len(self.buildingData[buildingName][floorName][room]) > 0:
                allRoomEmpty = False
        
        if allRoomEmpty:
            print("All rooms are vacant..!!")
            return
        
        for room in self.buildingData[buildingName][floorName]:
            for slot in self.buildingData[buildingName][floorName][room]:
                print( str(slot[0]) + ":" + str(slot[1]) + " " + floorName + " "  + buildingName + " " + room )
        return





    