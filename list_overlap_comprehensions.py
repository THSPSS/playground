#between two lists get common numbers between two list without duplicates
#working on list with different sizes
#randomly generate two lists to test this
import random

length_of_list = random.randint(3,10)
other_length_of_list = random.randint(3,10)
def main():
    print("list overlap comprehensions")
    a = random.sample(range(100), length_of_list)
    b = random.sample(range(100), other_length_of_list)
    print(a, b)
    if len(a) < len(b):
        shorter_list = a




if __name__ == "__main__":
    main()
