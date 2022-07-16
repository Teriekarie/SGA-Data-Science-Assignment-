# python program for assignment Module1,lesson3
# python program to assign intergers

x = (int(input("Enter 1st number")))
y = (int(input("Enter 2nd nummber")))

# program to check if the power is 0
def check_pow(x, y):
    if y == 0:
        return 1
    else:
       x **= y 
    return x
print(check_pow(x, y))

