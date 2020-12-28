class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


p = Point()
q = Point()


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "a {self.color} car".format(self=self)


my_car = Car("blue", 12345)


# print(my_car)

class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def __str__(self):
        return "my obj name is MyTime"


def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
    sum_t = MyTime(h, m, s)
    return sum_t


current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 14, 0)
done_time = add_time(current_time, bread_time)
print(done_time.hours)
