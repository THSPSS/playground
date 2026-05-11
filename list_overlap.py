import random

a = [random.randint(1,40) for _ in range(random.randint(10,15))]
b = [random.randint(1,40) for _ in range(random.randint(10,15))]
print(a,b)
result_list = []

def main():
    for num in a :
        if num in b and num not in result_list:
            result_list.append(num)


    print(result_list)


if __name__ == "__main__":
    main()