# * allows any number of arguments to be added
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

def main():
    print(add(1, 5, 6, 10))

    calculate(2, add=3, multiply=5)

    class Car:
        def __init__(self, **kw):
            self.make = kw.get("make")
            self.model = kw.get("model")

    my_car = Car(make="Nissan", model="GT-R")
    print(my_car.model)
    print(my_car.make)

    my_car_two = Car(make="Ford")
    print(my_car_two.model)
    print(my_car_two.make)

if __name__ == "__main__":
    main()