import random

numbers = []

def sort():
    for c in range(5):
        n = random.randint(0, 20)
        numbers.append(n)
    print(f"Sorted numbers: {numbers}")

def pluspair():
    plus = sum(n for n in numbers if n % 2 == 0)
    print(f"Soma dos pares: {plus}")


sort()
pluspair()


