import random
# Write a program that takes a list of numbers (for examples, a = [5, 10, 15, 20, 25] and makes a new list
# of only the first and last elements of the given list.
# For practice, write this code inside a function:

# 1. takes a list of numbers
# 2. get the first and last element of list


def list_ends():
    #generate random number list
    origin_list = random.sample(range(10), 9)
    last_element = origin_list.pop()
    new_list = [origin_list[0], last_element]
    print("new_list : ", new_list)
    # new_list = [ origin_list(x) if x == 0 for x in range(len(origin_list))]


if __name__ == "__main__":
    list_ends()