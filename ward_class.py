from occupancy_utils import log_update

class Ward:
    def __init__(self, name, total_beds, occupied_beds=0):
        self.name = name
        self.total_beds = total_beds
        self.occupied_beds = occupied_beds

    @log_update
    def admit(self, number=1):
        """Admit a patient with validation"""
        if self.occupied_beds + number <= self.total_beds:
            self.occupied_beds += number
            print(f"{number} patient(s) admitted to {self.name}")
        else:
            print(f"Cannot admit to {self.name} — ward is full!")

    @log_update
    def discharge(self, number=1):
        """Discharge a patient with validation"""
        if self.occupied_beds - number >= 0:
            self.occupied_beds -= number
            print(f"{number} patient(s) discharged from {self.name}")
        else:
            print(f"Cannot discharge from {self.name} — no patients!")

    def get_occupancy_rate(self):
        """Calculate occupancy percentage"""
        return (self.occupied_beds / self.total_beds) * 100
