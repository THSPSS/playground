#fibonacci number
#Finbonnaci sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#the sequence looks like this: 1,1,2,3,5,8,13....

def function():
    times = 0
    start_number = 1
    fibonnaci_list = [start_number, start_number+0]

    while times == 0:
        times = input("How many Fibonnaci numbers do you want to generate? : ")
        times = int(times)

        if times == 1:
            print([1])
            break
        if times == 2:
            print([1,1])
        for i in range(0, times-1):
            print(i)
            print(fibonnaci_list)
            fibonnaci_list.append(fibonnaci_list[len(fibonnaci_list)-1] + fibonnaci_list[len(fibonnaci_list)-2])

    # get current number from fibonnaci list

    # -1과 -2가 null 값일때는 그냥 + 1 하기
    #현재 주소에서 -1 , -2 한 것의 값을 현재 주소에 집어넣으면 됨
    #using while loop?






if __name__ == "__main__":
    print("this is main from fibonacci")
    function()