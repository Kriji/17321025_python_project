# Методите може да бъдат два вида класови методи (class methods) и методи на инстанцията
# (instance methods). Забележете, че class методите нямат self като параметър, а instance # методите задължително имат self. Също така class методите се използват като се използва # името на  класът
# MyClass.class_method(), а instance методите се използват като се използва името на обект
# създаден от даденият клас

class Company:
  """ В Този клас Company правим нашата комапния реална.
      Тук пазим името на комапнията, бонус точките на брокера и списък
      с всички брокери, които рабият в нея. 
  """

  def __init__(self, name): 
    self.name = name
    self.daily_bonus = 0
    self.brokers_list = []
    
  # създаваме Instance Method, който принтира информация за брокерите  
  def print_brokers(self):
    if(len(self.brokers_list) >= 1): # Ако имаме поне дин брокер на смяна принтираме информацията за него
      print(f"All brokers on shift in company {self.name} are: ")
      for broker in self.brokers_list:
        print(end=" | ")
        broker.print_broker_info()
      print()
    else: # Ако нямаме брокери на смяна казваме, че компанията е затворена. 
      print("Company is closed\n")

  # създаваме Instance Method - Добавяне на служители в компанията за конкретната смяна
  def add_brokers(self, *broker: object): 
    self.brokers_list += broker

  # Instance Method - Приключване на смяната на брокера. 
  def end_shift(self, broker_name: str):
    for n, broker in enumerate(self.brokers_list): # enumerate() - дoбавя index към всеки item в списъка. 
      if broker.name.lower() == broker_name.lower(): # Проверяваме дали подаденото име на брокера съвпада с име в списъка ни. 
        self.daily_bonus = broker.check_bonus_points() * 10
    
        if(self.daily_bonus > 0):
          print(f"{broker.name} has {self.daily_bonus}$ daily bonus\nGoodbye, see you tomorrow!\n")
          
        else:
          print (f"Sorry {broker.name}, but yor daily bonus is 0\nGoodbye, see you tomorrow!\n")

        self.brokers_list.remove(broker)
      
