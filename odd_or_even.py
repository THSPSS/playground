def get_two_answers_from_user(answers : str) -> tuple[str,str]:
    num_answer = answers.split()[0]
    check_answer =  answers.split()[1]
    return num_answer , check_answer


def check_if_number_is_time_4(input_number : int) -> bool:
    if input_number % 4 == 0 :
        return True
    else:
        return False


def check_odd_or_even(input_number:int)-> str:
    if input_number % 2 == 0 :
        return f"{input_number} is even"
    else:
        return f"{input_number} is odd"


def convert_string_into_int(input_string:str) -> int | None:
    try:
        return int(input_string)
    except ValueError:
        print("Please enter numbers only")
        return None

def asking_user_and_getting_data(question : str) -> str:
    return input(question)


def main() :
    #1. asking user number
    number = None

    #2. divide user number with 2 and check remainder
    while number is None :
        user_input = asking_user_and_getting_data("Please enter a number : ")
        number = convert_string_into_int(user_input)

    #3-1. check if number is multiple of 4
    if check_if_number_is_time_4(number):
        print (f"{number} is multiple number of 4")
    else :
        #3-2. if remainder is 0 than it is even otherwise it is odd
        result = check_odd_or_even(number)
        print(result)

if __name__ == "__main__":
    random_string = "302 2433"
    print(random_string.split()[0])
    # main()

