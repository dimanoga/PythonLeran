class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x + self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError("Wrong obj")

    def __eq__(self, room_obj):
        if isinstance(room_obj, Room):
            return True if self.area == room_obj.area else False
        raise TypeError("Wrong obj")


r1 = Room(3, 5)
r2 = Room(4, 7)
print(r1.area)
print(r2.area)
print(r1 + r2)
print(r1 == r2)
