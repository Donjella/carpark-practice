from classes.parking_slot import ParkingSlot
from classes.car import Car

#(carpark) to know which carpark the parking slot is added into
def add_slot(carpark):
    #take input the id for the parking slot
    slot_id = input("Enter the id for parking slot: ")
    #create an instance of the parking slot using the id above - to create an instance, we need to first import parking_slot.py
    parking_slot = ParkingSlot(slot_id)
    # add that slot to the carpark - by using additional method in the carpark.py itself,
    # instead of directly assessing properties, i.e. directly just using .append(slot)
    carpark.add_slot(parking_slot)
    print ("Parking Slot added\n")

def list_slots(carpark):
    # give listing responsibility to the carpark
    # or we can get the slots from the carpark and list it here
    # all_slots is a list, so we can use for-in loop, to loop through the list since get_slots() in carpark.py is a list
    all_slots = carpark.get_slots()
    print("Listing slots..")
    # if not all_slots = if all_slots do not have a value since empty list is a falsy value
    if not all_slots:
        print("No slots found.")
    for slothaha in all_slots:
        print(slothaha)
    print("\n")

def delete_slot(carpark):
    # take input the id of the parking slot
    slot_id = input("Enter the id of the parking slot: ")
    # delete the parking slot
    if carpark.delete_slot(slot_id):
        print("Parking slot deleted\n")
    else:
        print("No parking slot with that id\n")
    
def park_car(carpark):
    print("Parking a car")
    # take input the rego of the car
    reg_no = input("Enter the registration number of the car: ")
    # take id of slot you want to park
    slot_id = input("Enter the id of the parking slot: ")
    # find the parking slot to make sure it exist to park
    slot_to_park = carpark.find_slot(slot_id)
    # if it exists:
    if slot_to_park:
        car_to_park = Car(reg_no)
    # add car to parking slot
        if (slot_to_park.add_car(car_to_park)):
            print("Car parked successfully\n")
    # to add the car, we need to create instance of the car with rego
        else:
            print("Car already parked in slot\n")
    else:
        print("Slot with that id does not exist\n")
