from datetime import datetime
current_year = datetime.now().year
is_this_keep_working = True
greeting_and_continue = input("Hello! We will see year that you turn 100! Please Enter if you want to continue:)")

while is_this_keep_working:
    if greeting_and_continue=="":
        age = "0"
        is_contain_char = True
        int_age = 0
        name = input("Enter your name : ")


        #convert string into integer :best way to convert string to integer
        while is_contain_char:
            age = input("Enter your age : ")
            try:
                int_age = int(age)
                is_contain_char = False
            except ValueError:
                print("Please enter only number")

        #1. calculate years left until 100
        # 100 - age
        years_left = 100 - int_age

        #2. get current year and add result from 1
        result = current_year + years_left
        result_string = f"{name} ! You become 100 years in {result}! :)"


        #3. show user the result using print
        print(result_string)

        #4. ask user another random number
        repeat_times = input("Enter any number you like : ")

        print("repeat times" , repeat_times)


        #print out previous
        for i in range(0, int(repeat_times)):
            print(result_string)



