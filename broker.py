
class Broker():
  def __init__(self, name, age): # конструктор на класа Broker. 
    self.name = name # в main.py казваме името на брокера. 
    self.age = age # в main.py казваме брокера на колко години е
    self.experience = 0 # При продаване на сграда получаваме бонус точки
    self.buildings_list = [] # създаваме списък, който ще съдържа сградите на брокера, които може да продава. 

  # instance метод - Информация за брокер
  def print_broker_info(self):
    print (f"Broker name: {self.name} - age {self.age} - experience: {self.experience}")

  # instance метод - Добавяне на сграда в листа на съответния брокер
  def add_building(self, *building: object):
    self.buildings_list += building

    #print(len(building)) | output: 3, 1, 1
    if len(building) > 1: # Броят на сградите > 1
      print(f"New buildings have been added in {self.name}'s list:")
      # Arholl Arena, DSK Bank, Matt Hann
      #for building_item in self.buildings_list[-len(building):]:
      for building_item in self.buildings_list:
        print(end=" | ")
        building_item.print_building()
    else:
        print(f"New building has been added in {self.name}'s list:", end="\n | ")
        self.buildings_list[0].print_building()
    print() # нов ред след списъка с брокери за по-добра четимост.
  

  # instance метод - Принтиране на всички сгради в листа
  def print_all_buildings(self):
      
      if (len(self.buildings_list) != 0):
        print(f"All buildings in {self.name}'s list are:")
        for building in self.buildings_list:
            print(end=" | ")
            building.print_building()
      else:
        print (f"!!!Sorry but {self.name}'s list is Empty!!!")
      print() # добавям празен рез, за да се чете по-добре изходът
      

  # instance метод - Продаване на сграда. Използваме го в main.py             
  def sell_building(self, _building_name: str):
    sell = None
    #  n - Номер; building - сграда в dictionary от key-n и value-building 
    for n, building in enumerate(self.buildings_list):
      if building.building_name.lower() == _building_name.lower():
        sell = self.buildings_list[n]
        if building.is_expensive() == 10:
          self.experience += 10
          print (f"Congratulations, {self.name}!\nYou have 10 new points for selling \"{_building_name}\"\n---------------")
        else:
          self.experience +=5
          print (f"Congratulations, {self.name}!\nYou have 5 new points for selling \"{_building_name}\"\n---------------")
        self.buildings_list.remove(building)
        break
         
    if sell is not None:
      return sell # sell = self.buildings_list[n]
    else:
      print(f"!!! Sorry, {self.name} This building is not in your list, maybe it has been sold!!!\n")
      #return None

 # instance метод - за проверка на бонус точките на брокерите. 
  def check_bonus_points(self): #използваме го в company.py
    bonus_points = self.experience
    print(f"{self.name}'s total bonus points: {bonus_points}")
    return bonus_points
  
