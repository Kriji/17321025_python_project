class Building():
  """ В този клас има instance method is_expensive, според който брокерите взимат бонус точки. Ако сградата е по-скъпа от 500_000 взима +10 точки, а ако е по 500_000 взима +5 бонус точки. """

  # конструктор за клас Building.  Конструктор в Python се обявява като пренапишем методът __init__ с параметър self и всички параметри, които искаме да подадем при създаването на обекта. Self параметърът, ни дава достъп до данните на обекта върху, който се извиква методът
  def __init__(self, building_name, floors, price: float):
    self.building_name = building_name
    self.floors = floors
    self.price = price
    #self.sell_points = 0

  # instance method за принтиране на информация за сградата - име, етажи и цена
  def print_building(self):
    print(f"{self.building_name} - {self.floors} floors - {self.price:.2f}$")

  # Проверяваме дали сграда е скъпа (В зависимост от това варират бинус точките, които брокерът може да получи при продаването й). Използаваме го в broker.py - Instance method sell_building. 
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
