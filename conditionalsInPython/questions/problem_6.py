# Question_6

# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


while True:
    
    distance = int(input("Pls Enter the vaue of distance(in 'KiloMeters'): "))

    if distance < 3:
        print("Walk")
    elif distance < 16:
        print("Bike")
    elif distance > 15:
        print("Car")