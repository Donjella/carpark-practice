class Carpark:
    def __init__(self, name):
        self.name = name
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)

    def get_slots(self):
        return self.slots
    
    def delete_slot(self, slot_id):
        new_slots = []
        is_deleted = False
        for funny in self.slots:
            if funny.id != slot_id:
                new_slots.append(funny)
            else:
                is_deleted = True
        self.slots = new_slots
        return is_deleted