days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
temperatures = []

for day in days:
    temp = int(input(f"Enter Temperature of {day}: "))
    temperatures.append(temp)

fahrenheit = []

for day, C in zip(days, temperatures):  
    F = (C * 9/5) + 32
    fahrenheit.append(F)
    print(f"{day}: {C}°C = {F}°F")

avg_c = sum(temperatures) / len(temperatures)
avg_f = sum(fahrenheit) / len(fahrenheit)

print(f"\nAverage: {avg_c}°C = {avg_f}°F")