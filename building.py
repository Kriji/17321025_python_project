class Building():
  
  def __init__(self, building_name, floors, price: float):
    self.building_name = building_name
    self.floors = floors
    self.price = price
    #self.sell_points = 0

  def print_building(self):
    print(f"{self.building_name} - {self.floors} floors - {self.price:.2f}$")

  # Проверяваме дали сграда е скъпа (В зависимост от това варират бинус точките, които брокерът може да получи при продаването й)
  def is_expensive(self):
    sell_points = 0
    if self.price < 500000:
      print(f"Building - {self.building_name} is not expensive. \nPrice is: {self.price:.2f}$")
      sell_points =+ 5
      return sell_points
    elif self.price >= 500000:
      print(f"Building - {self.building_name} is expensive. \nPrice is: {self.price:.2f}$")
      sell_points =+ 10
      return sell_points
