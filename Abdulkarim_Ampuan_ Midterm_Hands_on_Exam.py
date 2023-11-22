import random

random_num1 = random.randint(1, 99)
random_num2 = random.randint(1, 99)

print("Random numbers from 1-99:")
print("Random 1:", random_num1)
print("Random 2:", random_num2)

ran1 = eval(input(f"What is {random_num1} + {random_num2}?"))
res = random_num1 + random_num2
print((random_num1), "+", (random_num2), "=", res)

if ran1 == res:
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. Please try again.")


ran_num1 = random.randint(1, 99)
ran_num2 = random.randint(1, 99)

print("Random numbers from 1-99:")
print("Random 1:", ran_num1)
print("Random 2:", ran_num2)

x1 = eval(input(f"What is {ran_num1} - {ran_num2}?"))
a1 = ran_num1 - ran_num2
print((ran_num1), "-", (ran_num2), "=", a1)

if ran1 == res:
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. Please try again.")


num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

print("Random numbers from 1-99:")
print("Random 1:", num1)
print("Random 2:", num2)

y1 = eval(input(f"What is {num1} * {num2}?"))
a2 = num1 * num2
print((num1), "*", (num2), "=", a2)

if y1 == a2:
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. Please try again.")


val1 = random.randint(1, 99)
val2 = random.randint(1, 99)

print("Random numbers from 1-99:")
print("Random 1:", val1)
print("Random 2:", val2)

z1 = eval(input(f"What is {val1} / {val2}?"))
a3 = val1 / val2
print((val1), "/", (val2), "=", a3)

if z1 == a3:
    print("Your answer is correct!")
else:
    print("Your answer is incorrect. Please try again.")