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
          
	def __eq__(self, other):
		if isinstance(other,int):
			return self.number_of_floor==other
		elif isinstance(other,House):
			return self.number_of_floor==other.number_of_floor
		return "невозможно сравнить разные типы данных"
		
	def __lt__(self, other):
		if isinstance(other,int):
			return self.number_of_floor<other
		elif isinstance(other,House):
			return self.number_of_floor<other.number_of_floor
		return "невозможно сравнить разные типы данных"
		
	def __le__(self, other):
		if isinstance(other,int):
			return self.number_of_floor<=other
		elif isinstance(other,House):
			return self.number_of_floor<=other.number_of_floor
		return "невозможно сравнить разные типы данных"
		
	def _gt_(self, other):
		if isinstance(other,int):
			return self.number_of_floor>other
		elif isinstance(other,House):
			return self.number_of_floor>other.number_of_floor
		return "невозможно сравнить разные типы данных"
		
	def __ge__(self, other):
	    if isinstance(other,int):
	    	return self.number_of_floor>=other
	    elif isinstance(other,House):
	    	return self.number_of_floor>=other.number_of_floor
	    return "невозможно сравнить разные типы данных"
	    
	def _ne__(self, other):
	    if isinstance(other,int):
	    	return self.number_of_floor!=other	    	
	    elif isinstance(other,House):
	    	return self.number_of_floor!=other.number_of_floor
	    return "невозможно сравнить разные типы данных"
	    
	def __add__(self, other):
	    if isinstance(other,int):
	    	self.number_of_floor+=other
	    return self
	    
	def __ladd__(self, other):
	    if isinstance(other,int):
	    	self.number_of_floor=self.number_of_floor+other
	    return self
	    
	def __radd__(self, other):
	    if isinstance(other,int):
	    	self.number_of_floor=other+self.number_of_floor
	    return self
        
    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
