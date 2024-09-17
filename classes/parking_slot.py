class ParkingSlot:
    def __init__(self, id):
        self.id = id
        self.car = None

    def __str__(self):
        #  if self.car: - means if self.car is present, i.e. a car is present or self.car != none
        if self.car:
            return f"Parking slot with id {self.id} and has the following car: {self.car}"
        else:
            return f"Parking slot with id {self.id} and has no car parked"
        
     