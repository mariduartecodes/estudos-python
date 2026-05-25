base_fee = 400

km = int(input("How many km of travel? "))

if km <= 50:
    travel_cost = 0
elif km <= 100:
    travel_cost = 100
elif km <= 200:
    travel_cost = 300
else:
    travel_cost = 2000

audience_size = int(input("How many people at the concert? "))
if 1000 <= audience_size <= 5000:
    equipment_cost = 2000
elif audience_size > 5000:
    equipment_cost = 10000
else:
    equipment_cost = 0


duration_minutes = int(input("How many minutes will the show last? "))
if duration_minutes <= 120:
    time_extra = 0
elif duration_minutes <= 180:
    time_extra = 200
else:
    time_extra = 1000

total_fee = int((base_fee + travel_cost + equipment_cost + time_extra)*1.1)

print("-"*20)
print(f"TOTAL FEE: R${total_fee}")
print(f"EQUIPMENT COST: R${equipment_cost}\n")
print("Thank you! =^.^=")
print("-"*20)