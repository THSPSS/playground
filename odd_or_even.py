
def check_odd_or_even(input_number:int)-> str:
    if input_number % 2 == 0 :
        return f"{input_number} is even"
    else:
        return f"{input_number} is odd"


def convert_string_into_int(input_string:str) -> int:
    try:
        return int(input_string)
    except ValueError:
        print("Please enter numbers only")
        return 0

def asking_user_and_getting_data(question : str) -> str:
    return input(question)


def main() :
    #1. asking user number
    number = 0
    print("this is main")

    #2. divide user number with 2 and check remainder
    while number == 0 :
        user_input = asking_user_and_getting_data("Please enter number : ")
        number = convert_string_into_int(user_input)

    #3. if remainder is 0 than it is even otherwise it is odd
    result = check_odd_or_even(number)

    print(result)

if __name__ == "__main__":
    main()

