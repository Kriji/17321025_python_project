from broker import Broker
from building import Building
from company import Company

# [Сгради] - Създаваме сгради:
building_1 = Building("Arholl Arena", 7, 500601.71)
building_2 = Building("DSK Bank HQ", 8, 3000000)
building_3 = Building("Maria's diner", 1, 5732.97)
building_4 = Building("Matt Hann",4, 4242)
building_5 = Building("Balkan Hotel", 6, 1500000.00)
building_6 = Building("Disko BG", 2, 430034)

# [Брокери] - създаваме брокерите:
broker_1 = Broker("Natali", "45")
broker_2 = Broker("George", "27")
broker_3 = Broker("Jasmin", "30")
broker_4 = Broker("Stefan", "43")

#Създаваме компанията, в която работят нашите брокери
company = Company("MATTAHAN")

#Добавяме брокерите на смяна
company.add_brokers(broker_1, broker_2, broker_3, broker_4)
company.print_brokers() #проверяваме кои брокери са на смяна

print("******** LETS SELL SOME BUILDINGS ********\n")

broker_1.add_building(building_1, building_2, building_4)
broker_2.add_building(building_3)
broker_3.add_building(building_5)

broker_1.print_all_buildings()
broker_2.print_all_buildings()


print ("========================================")

broker_1.sell_building("Matt Hann")
broker_1.sell_building("Arholl Arena")
broker_2.sell_building("Maria's diner")
broker_3.sell_building("Balkan Hotel")

print ("========================================")

company.print_brokers()
company.end_shift("Natali")
company.end_shift("Stefan")
company.end_shift("George")
company.end_shift("Jasmin")

company.print_brokers()
