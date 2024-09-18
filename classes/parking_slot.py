class ParkingSlot:
    def __init__(self, id):
        self.id = id
        self.car = None

    def add_car(self, car):
        if self.car:
            return False
        else:
            self.car = car
            return car

    def get_car(self):
        return self.car

    def get_id(self):
        return self.id
    def __str__(self):
        #  if self.car: - means if self.car is present, i.e. a car is present or self.car != none
        if self.car:
            return f"Parking slot with id {self.id} and has the following car: {self.car}"
        else:
            return f"Parking slot with id {self.id} and has no car parked"
        
     