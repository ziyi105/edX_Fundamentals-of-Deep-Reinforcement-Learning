import random
import numpy as np

# 3 levels

a = 3
Q = [0] * a
N = [0] * a
epsilon = 0.3

# Initializing levels
def level_1():
    random_number = random.random()
    if random_number > 0.5:
        return 1
    return 0

def level_2():
    random_number = random.random()
    if random_number > 0.7:
        return 1
    return 0

def level_3():
    random_number = random.random()
    if random_number > 0.2:
        return 1
    return 0

def bandit(A):
    if A == 1:
        return level_1()
    elif A == 2:
        return level_2()
    return level_3()

loop = 0
while loop < 100:
    random_number = random.random()
    if random_number > epsilon:
        A = np.argmax(Q)
    else:
        random_level = random.randint(0, 2)
        A = random_level

    R = bandit(A)
    N[A] = N[A] + 1
    Q[A] = Q[A] + 1/N[A] * (R - Q[A]) 
    loop += 1 

print("N: ", N)
print("Q: ", Q)