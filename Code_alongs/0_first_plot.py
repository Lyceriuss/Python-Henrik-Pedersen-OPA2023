import matplotlib.pyplot as plt

numbers = list(range(11))

squares = [number**2 for number in numbers]

print(numbers)
print(squares)

plt.plot(numbers,squares)
plt.title("x2 for positive integers 0-10")
plt.xlabel("x")
plt.ylabel("y")
plt.show()