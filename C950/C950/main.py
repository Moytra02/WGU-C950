# Artyom Basov
# Student ID: 006954686
# WGUPS Routing Program

import datetime
from Package import packageHashTable
from Truck import truck1, truck2, truck3, getTruckAssignedToPackage

print("****************************************************")
print("Western Governors University Parcel Service (WGUPS)")
print("****************************************************")
print("*************")
print("The total mileage for the completed route is:")
print(truck1.mileage + truck2.mileage + truck3.mileage)
print("*************")
print("truck 1 completed delivery at: ", truck1.time)
print("truck 3 completed delivery at: ", truck3.time)
print("truck 2 completed delivery at: ", truck2.time)
print("*************")
print("*************")

# option 1: print all package data at a given time
def checkAllPackageStatus(time):
    for id in range(1,41):
        package = packageHashTable.getValue(id)
        package.currentStatus(time)
        package.updateAddress(time)
        if package.status == "delivered":
            truck = getTruckAssignedToPackage(package.ID)
            print(f"Package ID: {package.ID} | Delivery Deadline: {package.deadline} | Delivery Address: {package.deliveryAddress}")
            print(f"    Package status: delivered at {package.deliveryTime} to {package.deliveryAddress} on Truck {truck.truckID}")
        elif package.status == "out for delivery":
            if truck is not None:
                print(f"Package ID: {package.ID} | Delivery Deadline: {package.deadline} | Delivery Address: {package.deliveryAddress}")
                print(f"    Package Status: out for delivery. Currently located on truck {truck.truckID} at {truck.address}")
            else:
                print("package not assigned to any truck")
        else:
            truck = getTruckAssignedToPackage(package.ID)
            print(f"Package ID: {package.ID} | Delivery Deadline: {package.deadline} | Delivery Address: {package.deliveryAddress}")
            print(f"     Package Status: at hub, 4001 S 700 E. Assigned to truck {truck.truckID}")

# option 2: print data for certain ID at a give time
def checkOnePackageStatus(packageID, time):
    package = packageHashTable.getValue(packageID)
    package.updateAddress(time)
    if package is None:
        print("No package found with ID: ", packageID)
        return
    package.currentStatus(time)
    truck = getTruckAssignedToPackage(package.ID)
    print(f"Printing all package info for ID#{package.ID}:")
    print(f"*********")
    print(f"Current Status: {package.status}")
    if package.status == "delivered":
        print(f'Delivered at {package.deliveryTime} to {package.deliveryAddress}')
    elif package.status == "out for delivery":
        print(f'Current Location: {truck.address} on truck {truck.truckID}')
    else:
        print("preparing for delivery")

    print(f'Delivery Deadline: {package.deadline}')
    print(f'Delivery Address: {package.deliveryAddress}, {package.city}, {package.state}, {package.Zip}')
    print(f'Package Weight(kg): {package.weight}')
    print(f'Special Notes (optional): {package.notes}')

print("Welcome to the WGUPS package status check interface.")
input_time = input("Please enter the time (HH:MM:SS format): ")
hour, minute, second = input_time.split(":")
time_entered = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
branch_input = input("Would you like to view the status of an individual package? (y/n): ")
if branch_input == "y":
    try:
        id_input = int(input("Please enter the package ID: "))
        package = packageHashTable.getValue(id_input)
        checkOnePackageStatus(id_input, time_entered)
    except ValueError:
        print("Please enter a valid package ID.")
elif branch_input == "n":
    try:
        print("Current status of all packages at ", time_entered, ":")
        checkAllPackageStatus(time_entered)
    except ValueError:
        print("invalid input :( please try again.")
        exit()
else:
    exit()