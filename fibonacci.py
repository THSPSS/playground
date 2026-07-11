#fibonacci number
#Finbonnaci sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#the sequence looks like this: 1,1,2,3,5,8,13....

def function():
    times = 0
    number = 1

    while times == 0:
        times = input("How many Fibonacci numbers do you want to generate? : ")
        times = int(times)

    if times == 1:
        fibonacci_list = [1]
    elif times == 2:
        fibonacci_list = [1, 1]
    elif times > 2:
        fibonacci_list = [1, 1]
        while number < (times - 1):
            fibonacci_list.append(fibonacci_list[number] + fibonacci_list[number-1])
            number += 1
    return fibonacci_list

    # get current number from fibonnaci list

    # -1과 -2가 null 값일때는 그냥 + 1 하기
    #현재 주소에서 -1 , -2 한 것의 값을 현재 주소에 집어넣으면 됨
    #using while loop?






if __name__ == "__main__":
    final_list = function()
    print(final_list)