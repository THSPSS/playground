def get_integer():
    return int(input("Give me a number: "))

def is_even(num):
    return num % 2 == 0

def check_primality():
    num = get_integer()
    result = []
    if is_even(num):
        return "This is not prime number"

    for i in range(2, num - 1):
        if num % i == 0:
            result.append(i)
    if len(result) == 0:
        return "This is prime number"
    else:
        return "This is not Prime number"


if __name__ == "__main__":
    print("init")
    print(check_primality())