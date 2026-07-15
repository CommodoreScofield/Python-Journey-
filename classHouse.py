class House:
    
    def __init__(self, h_no, h_size, h_room, h_price ):
        self.__h_no = h_no
        self.__h_size = h_size
        self.__h_room = h_room
        self.__h_price = h_price

    def get_h_no(self):
        return self.__h_no
    
    def get_h_size(self):
        return self.__h_size
    
    def get_h_room(self):
        return self.__h_room
    
    def get_h_price(self):
        return self.__h_price
    
    def set_h_no(self,no):
        self.__h_no = no

    def set_h_size(self,size):
        self.__h_size = size

    def set_h_room(self,room):
        self.__h_room = room
    
    def set_h_price(self,price):
        self.__h_price = price

    
    
def main():
    h_1 = House("01", "60X40", 3 , 120000)
    h_2 = House("02", "60X10", 1 , 10000)
    h_3 = House("03", "100X40", 3 , 120000)

    house_class = [h_1, h_2, h_3]
    print(f"------------*-----------------*---------------------*")

    for house in house_class:
        print(f"{house.get_h_no()} {house.get_h_size()} {house.get_h_room()} {house.get_h_price()}")

    h_1.set_h_price(1600000)
    h_2.set_h_price(2200000)
    h_3.set_h_price(5600000)
    print(f"------------*-----------------*---------------------*")

    for house in house_class:
        
        print(f"{house.get_h_no()} {house.get_h_size()} {house.get_h_room()} {house.get_h_price()}")

    print(f"------------*-----------------*---------------------*")
 
main()
