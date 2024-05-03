import random

def random_numbers_list():
    num_list = []
    for x in range(0, 100000):
        random_number = random.randint(0, 100)
        num_list.append(random_number)
    return num_list
