Ho = 70
distance = 0

def calculator(distance):
    v = Ho * distance
    return v

while True:
    distance = float(input("Enter the galaxy's distance from Earth (in Megaparsecs)"))
    if distance > 0:       
        result = calculator(distance)
        print(f"Recession speed: {result:.2f} km/s")
    else:
        break

