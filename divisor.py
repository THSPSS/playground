# if user input is 4
# 1, 2 , 4 is divisor of 4 약수를 찾아라
# list를 1부터 해당 숫자까지 포함할 수 있게 만듬
# list를 돌면서 user_input 넘버와 각 element를 나누어 remainder가 0인지 확인
from odd_or_even import asking_user_and_getting_data, convert_string_into_int


def main():
    #get a number from user
    int_number = None
    user_input = asking_user_and_getting_data("Please enter a number : ")
    while int_number is None:
        int_number = convert_string_into_int(user_input)
    if int_number == 1 :
        return print("divisor of" , int_number , "is itself" )
    range_list = range(1, int_number)
    divisor_list = [ num for num in range_list if int_number % num == 0]
    # for num in range_list:
    #     if int_number % num == 0:
    #         divisor_list.append(num)

    return print("divisor of" , int_number , "is" , divisor_list)

if __name__ == "__main__":
    main()