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
     
    def __len__(self):
             return self.number_of_floor
      
    def __str__(self):
         return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')     


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
