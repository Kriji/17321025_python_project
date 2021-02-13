# Тематиката на програмата е продаваме сгради. 
# 1) В началото създаваме сградите, които искаме да продаваме
# 2) След това създаваме нашите брокери, които ще продават
# 3) И накрая създаваме компанията си, в която работят напите брокери
# -----------
# Всеки ден има различни брокери, които са на смяна. След като сме казали, кои искаме
# да са на смяна, добавяме и кои сгради искаме всеки един да продаде. 
# При продаването на сградата има значение тя колко струва. В зависомост от това се 
# трупат точки и нашите брокери получват бонус в края на смяната си. 
# 

from broker import Broker
from building import Building
from company import Company

# [Сгради] - Създаваме ОБЕКТИ за сградите (buildin_1, buildin_2....):
building_1 = Building("Arholl Arena", 7, 500601.71)
building_2 = Building("DSK Bank", 8, 3000000)
building_3 = Building("Maria's diner", 1, 5732.97)
building_4 = Building("Matt Hann",4, 4242)
building_5 = Building("Balkan Hotel", 6, 1500000.00)
building_6 = Building("Disko BG", 2, 430034)

# [Брокери] - създаваме ОБЕКТИ за брокерите (broker_1, broker_2...):
broker_1 = Broker("Natali", "45")
broker_2 = Broker("George", "27")
broker_3 = Broker("Jasmin", "30")
broker_4 = Broker("Stefan", "43")

#Създаваме ОБЕКТ company
company = Company("MATTAHAN")

#Добавяме брокерите на смяна
company.add_brokers(broker_1, broker_2, broker_3, broker_4) # извикваме instance метода add_broker върху обекта company 
company.print_brokers() # проверяваме кои брокери са на смяна, като извикваме instance метода pritn_brokers върху обекта comany

print("******** LETS SELL SOME BUILDINGS ********\n")

# Добавяме сградите, които искаме да бъдат продадени от съответния брокер, като извикваме Instance метода add_building върху обекта (broker_1, broker_2...) на съответния брокер. 
broker_1.add_building(building_1, building_2, building_4)
broker_2.add_building(building_3)
broker_3.add_building(building_5)

# Проверяваме списъка със сгради - извикваме Instance метода print_all_buildings върху обекта за съответния брокер

broker_1.print_all_buildings()
broker_2.print_all_buildings()


print ("========================================")

# Продаваме съответната сграда. 
broker_1.sell_building("Matt Hann")
broker_1.sell_building("Arholl Arena")
broker_2.sell_building("Maria's diner")
broker_3.sell_building("Balkan Hotel")
broker_3.sell_building("Balkan Hotel") # опит за продаване на сграда, която не е в нашия списък. 

print ("========================================")

# Приключваме смяната на брокера и проверяваме колко бонус точки е натрупал всеки в края на смяната си - извикваме instance метода end_shift от клас Company върху обект company  
company.print_brokers()
company.end_shift("Natali")
company.end_shift("Stefan")
company.end_shift("George")
company.end_shift("Jasmin")

company.print_brokers()
