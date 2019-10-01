class Horse:
    def __init__(self, horse_name, rider):
        self.horse_name = horse_name
        self.rider = rider

class Rider:
    def __init__(self, rider_name):
        self.rider_name = rider_name

bantyo = Rider("番長")
tyoku = Horse("直線番長", bantyo)
print(tyoku.rider.rider_name)