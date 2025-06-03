import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [20, 22, 19, 23, 21, 24, 20]
plt.figure(figsize=(8, 4))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
plt.title('Weekly Temperature Readings')
plt.xlabel('Day of Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
