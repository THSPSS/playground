a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result_list = []

def main():
    for num in a :
        if num in b:
            result_list.append(num)
    # for num in b:
    #     if num in a:
    #         #check if it is there or not


if __name__ == "__main__":
    main()