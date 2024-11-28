class House():
    
    def __init__(self, name, number_of_floor):
        self.name=name
        self.number_of_floor= number_of_floor
        self.curent_floor=1
    def go_to(self, floor):
         if floor>self.number_of_floor or floor<1:
             print("Такого этажа не существует")
         else:
             while floor>0:
                 print(self.curent_floor)
                 self.curent_floor+=1
                 floor-=1
             


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)