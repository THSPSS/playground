#between two lists get common numbers between two list without duplicates
#working on list with different sizes
#randomly generate two lists to test this
import random

length_of_list = [1,4,2,5,13]
other_length_of_list = [3,5,5,20,1]
def main():
    print("list overlap comprehensions")
    a = [1,4,2,5,13]
    b = [3,5,5,20,1,10]

    result = []
    print(a, b)
    if len(a) < len(b):
        shorter_list = a
        longer_list = b
    else:
        shorter_list = b
        longer_list = b

    result = [num for num in shorter_list if num in longer_list]
    print(result)




if __name__ == "__main__":
    main()
