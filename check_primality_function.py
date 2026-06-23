def get_integer():
    return int(input("Give me a number: "))

def is_even(num):
    return num % 2 == 0

def check_primality():
    num = get_integer()

    if num > 0 :
        for i in range(2, num - 1):
            if num % i != 0:
                continue
            elif num % i == 0:
                print( "This number is not prime")
                break
    elif num == 0:
        print("This number is not prime")
    else:
        print("this number is not prime")





if __name__ == "__main__":
    check_primality()