#Question1
def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")
    
hello_name('Shawna')

#Question2
start, end = 0, 100

# iterating each number in list

for num in range(start, end +1):

    # checking condition
    if num % 2 != 0:
        print(num,end = " ")


#Question3
print('======================================================')
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([12,3,15,28,9])
print(max_num_in_list([12,3,15,28,9]))

#Question4
print('======================================================')
def is_leap_year(year) :
    if year % 400 == 0:
        return True
    if year % 100 == 0:
         return False
    if year % 4 == 0:
         return True 
    else:
     return False
    
print(is_leap_year(1922))
print(is_leap_year(2012))


#Question5
print('======================================================')
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print((status))