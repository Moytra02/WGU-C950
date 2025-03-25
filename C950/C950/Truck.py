import csv
import datetime
from Package import packageHashTable

class Truck:
    def __init__(self, packages, speed, mileage, address, departureTime, truckID):
        self.packages = packages
        self.speed = speed
        self.mileage = mileage
        self.address = address
        self.departureTime = departureTime
        self.time = departureTime
        self.truckID = truckID

    def __str__(self):
        return f'{self.packages}, {self.speed}, {self.mileage}, {self.address}, {self.departureTime}, {self.time}'

# read distance csv
with open("CSV/distance_file.csv") as distance_file:
    distance = csv.reader(distance_file)
    distance = list(distance)

# get addresses from csv
def getAddress(address):
    addressList = []
    with open('CSV/Address_File.csv') as address_file:
        addresses = csv.reader(address_file)
        for row in addresses:
            addressList.append(row[2])
    return addressList
addressList = getAddress('Address_File.csv')

def distanceBetween(x, y):
    I = addressList.index(x)
    J = addressList.index(y)
    distance_from = distance[I][J]
    if distance_from == '':
        distance_from = distance[J][I]
    return float(distance_from)

truck1 = Truck([1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 40], 18, 0, "4001 South 700 East", datetime.timedelta(hours=8),1)
truck2 = Truck([3, 8, 9, 12, 17, 18, 22, 23, 24, 27, 35, 36, 38, 39], 18, 0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20),2)
truck3 = Truck([2, 4, 5, 6, 7, 10, 11, 25, 26, 28, 31, 32, 33, 37], 18, 0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),3)

def deliverPackages(truck):
    notDelivered = []
    for pID in truck.packages:
        package = packageHashTable.getValue(pID)
        package.truckID = truck.truckID
        package.departureTime = truck.departureTime
        notDelivered.append(package)
    truck.packages.clear()
    while len(notDelivered) > 0:
        nextStop = 1000
        nextPackage = None
        for package in notDelivered:
            distanceNextStop = distanceBetween(truck.address, package.deliveryAddress)
            if distanceNextStop < nextStop:
                nextStop = distanceNextStop
                nextPackage = package
        if nextPackage is not None:
            nextPackage.deliveryTime = truck.time
            nextPackage.departureTime = truck.departureTime
            if nextPackage.ID == "9":
                nextPackage.updateAddress(nextPackage.ID, truck.departureTime)
            truck.packages.append(nextPackage.ID)
            notDelivered.remove(nextPackage)
            package.finalAddress = package.deliveryAddress
            truck.address = nextPackage.deliveryAddress
            truck.mileage += nextStop
            truck.time += datetime.timedelta(minutes=nextStop)

deliverPackages(truck1)
deliverPackages(truck3)
deliverPackages(truck2)

def getTruckAssignedToPackage(package_id):
    for truck in [truck1, truck2, truck3]:
        if package_id in truck.packages:
            return truck
    return None