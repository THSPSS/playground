import random

from odd_or_even import asking_user_and_getting_data, convert_string_into_int


#how about put random numbers in list that would be more fun

#for loop to check all the element in list
#check if element is less than 5
def main():
    user_number = None
    a = [random.randint(1, 45) for _ in range(11)]
    result_list = []


    while user_number is None:
        user_number = asking_user_and_getting_data("Please enter a number : ")

    int_user_number = convert_string_into_int(user_number)

    for num in a :
        if num < int_user_number :
            print(num)
            result_list.insert(num)

    print([num for num in a if num < 5])
    print(result_list)


if __name__ == "__main__":
    main()

