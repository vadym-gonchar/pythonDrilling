class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

        return print(x + y)

pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)

pt1 = Point()
pt1.set_coords(2, 3)
print(pt1.__dict__)