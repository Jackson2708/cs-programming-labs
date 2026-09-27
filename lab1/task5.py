distance_km = float(input())
fuel_per_100km = float(input())
price_per_liter = float(input())

fuel_needed = distance_km * fuel_per_100km / 100
total_cost = fuel_needed * price_per_liter

print(f"Топливо: {fuel_needed:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб")