from odd_or_even import asking_user_and_getting_data

a = [1,2,3]
backword_string_list = []
def main():
    user_string = asking_user_and_getting_data("Please Enter String : ")
    print(user_string == user_string[::-1])
    # start from end and to start
    # for i in range(len(user_string)-1,-1,-1):
    #     backword_string_list.append(user_string[i])
    #     # backword_string_list.append(a[i-1])
    # print(backword_string_list)
    # if user_string == ''.join(map(str, backword_string_list)):
    #     print(f"{user_string} is a palindrome!")


if __name__ == "__main__" :
    main()