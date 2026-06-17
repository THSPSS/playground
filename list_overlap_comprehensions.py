#between two lists get common numbers between two list without duplicates
#working on list with different sizes
#randomly generate two lists to test this
import random

length_of_list = [1,4,2,5,13]
other_length_of_list = [3,5,5,20,1]
def main():
    a = random.sample(range(10), 5)
    b = random.sample(range(10), 9)

    print("a", a)
    print("b", b)


    result = [num for num in a if num in b]
    print(result)




if __name__ == "__main__":
    main()
