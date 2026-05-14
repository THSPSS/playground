a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def main():
    print("this is main")
    new_list = [num for num in a if num % 2 == 0 ]
    print(new_list)


if __name__ == "__main__":
    main()