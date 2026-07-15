class Car:

    def __init__(self,make,model,year):

        self.make = make
        self.model = model
        self.year = year

    def __str__(self):

        return(f"{self.make} {self.model} {self.year}")

def main():

    car_1 = Car("Maruti","Alto",2011)
    car_2 = Car("Honda","City",2016)
    car_3 = Car("Toyota","Fortuner",2008)
    print(car_1.__str__())
    print(car_2.__str__())
    print(car_3.__str__())


main()

        