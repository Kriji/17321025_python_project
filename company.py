class Company:
  def __init__(self, name):
    self.name = name
    self.daily_bonus = 0
    self.brokers_list = []
    
  # Принтираме информация за брокерите  
  def print_brokers(self):
    if(len(self.brokers_list) >= 1):
      print(f"All brokers on shift in company {self.name} are: ")
      for broker in self.brokers_list:
        print(end=" | ")
        broker.print_broker_info()
      print()
    else:
      print("Company is closed\n")

  # Добавяне на служители в компанията за конкретната смяна
  def add_brokers(self, *broker: object):
    self.brokers_list += broker

  def end_shift(self, broker_name: str):
    for n, broker in enumerate(self.brokers_list):
      if broker.name.lower() == broker_name.lower():
        self.daily_bonus = broker.check_bonus_points() * 10
    
        if(self.daily_bonus > 0):
          print(f"{broker.name} has {self.daily_bonus}$ daily bonus\nGoodbye, see you tomorrow!\n")
          
        else:
          print (f"Sorry {broker.name}, but yor daily bonus is 0\nGoodbye, see you tomorrow!\n")

        self.brokers_list.remove(broker)
      
