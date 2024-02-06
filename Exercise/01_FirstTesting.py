import matplotlib.pyplot as plt

X = [0] * 2
Y = [0] * 2


for i in range(2):
    print(f"Variable number: {i+1}")
    X[i] = int(input("Enter variable X "))
    Y[i] = int(input("Enter variable Y "))

print("Coordinates:")
for i in range(2):
    print(f"({X[i]}, {Y[i]})")