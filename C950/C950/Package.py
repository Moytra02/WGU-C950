import csv
from HashTable import HashTable
import datetime

# package object information
class Package:
    def __init__(self, ID, deliveryAddress, city, state, Zip, deadline, weight, notes, status, truckID, finalAddress):
        self.ID = ID
        self.deliveryAddress = deliveryAddress
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.deliveryTime = None
        self.departureTime = None
        self.truckID = None
        self.finalAddress = None

    def __str__(self):
        return (f'ID: {self.ID},  delivery address: {self.deliveryAddress}, '
                f'city: {self.city}, state: {self.state}, zip: {self.Zip},'
                f' deadline: {self.deadline}, weight: {self.weight}, notes: {self.notes}, '
                f'status: {self.status}, truckID: {self.truckID}, finalAddress: {self.finalAddress}')

    # find status of package at any give time
    def currentStatus(self, time_entered):
        if self.deliveryTime < time_entered:
            self.status = "delivered"
        elif self.deliveryTime > time_entered and self.departureTime < time_entered:
            self.status = "out for delivery"
        else:
            self.status = "at hub"

    # update address for package 9 when address is corrected
    def updateAddress(self, time):  #
        if self.ID == 9 and time >= datetime.timedelta(hours=10, minutes=20):
            self.deliveryAddress = "410 South State Street"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.Zip = "84111"

# create hash table
packageHashTable = HashTable()

# create and load package data from csv
def createPackage(file):
    with open(file) as packages:
        data = csv.reader(packages, delimiter=',')
        for packages in data:
            pID = int(packages[0])
            pdeliveryAddress = packages[1]
            pcity = packages[2]
            pstate = packages[3]
            pZip = packages[4]
            pdeadline = packages[5]
            pweight = packages[6]
            pnotes = packages[7]
            pstatus = "at Hub"
            ptruckID = "not loaded"
            pfinalAddress = "undelivered"
            p = Package(pID, pdeliveryAddress, pcity, pstate, pZip, pdeadline, pweight, pnotes, pstatus, ptruckID,
                        pfinalAddress)
            packageHashTable.insert(pID, p)

file_path = 'CSV/packageCSV.csv'
createPackage(file_path)