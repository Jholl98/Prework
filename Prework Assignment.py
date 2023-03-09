#Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name): #Defined function
    print("Hello, " + user_name.title() + ".")

name = input("What is your name: ") #Input command for user
(hello_name(name))


#Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(): #Defined function
    num = 0 #variable
    while num <100: #While statement to count from 1 - 100
        num += 1
        if num % 2 == 0:
            continue
        print(num)

first_odds()



#Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list (a_List): #Defined function
    print(len(a_List))
num_list = [1,2,3,4,5,6,7,8,9,0] #determining the length of my list with int

max_num_in_list(num_list)


#Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year): #Defined function
 if((a_year % 400 == 0) or (a_year % 100 != 0) and (a_year % 4 == 0)): #Constraints for determining if a year is dividable by 4, not 100 unless by 400
    print("Is a leap year.")
 else: #Else the year is not a leap year
   print("Is not a leap year.")
Year = int(input("Enter the year: "))
is_leap_year(Year)



#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):#Defined function
    if len(a_list) < 1: #Making sure list is more > 1 int
        return False
    min_val = min(a_list) #minimum list
    max_val = max(a_list) #maximum list
    if max_val - min_val + 1 == len(a_list): #is the same as size of a_list
        for i in range(len(a_list)): #for i in range of 0 to a_list, do
            if a_list[i] < 0:
                j = -a_list[i] - min_val
            else:
                j = a_list[i] - min_val
                if a_list[j] > 0:
                    a_list[j] = -a_list[j]
                else:
                    return False 
            return True
        return False

a_list = [5,4,2,1,3,6,7,9,8,0]
print(is_consecutive(a_list))
    