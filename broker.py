
class Broker():
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.experience = 0 # При продаване на сграда получаваме бонус точки
    self.buildings_list = []

  # Информация за брокер
  def print_broker_info(self):
    print (f"Broker name: {self.name} - age {self.age} - experience: {self.experience}")

  # Добавяне на сграда в листа на съответния брокер
  def add_building(self, *building: object):
    self.buildings_list += building

    if len(building) > 1:
      print(f"New buildings have been added in {self.name}'s list:")
      for building in self.buildings_list[-len(building):]:
        print(end=" | ")
        building.print_building()
    else:
        print(f"New building has been added in {self.name}'s list:", end="\n | ")
        self.buildings_list[-1].print_building()
        print()
  
  # Принтиране на всички сгради в листа
  def print_all_buildings(self):
      
      if (len(self.buildings_list) != 0):
        print(f"All buildings in {self.name}'s list are:")
        for building in self.buildings_list:
            print(end=" | ")
            building.print_building()
      else:
        print (f"!!!Sorry but {self.name}'s list is Empty!!!")
      print() # добавям празен рез, за да се чете по-добре изходът
      

  # Продаване на сграда             
  def sell_building(self, _building_name: str):
    sell = None
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
      return sell
    else:
      print(f"!!! Sorry, {self.name} This building is not in your list, maybe it has been sold!!!\n")
      return None

  def check_bonus_points(self): #използваме го в company.py
    bonus_points = self.experience
    print(f"{self.name}'s total bonus points: {bonus_points}")
    return bonus_points
  
