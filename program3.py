#x = input("Type something here: ")
#print(x)
#y = input("Choose a number: ")
#z = input("Choose another number: ")
#sum = float(y) + float(z)
#print(sum)
def ask_for_input():
    number_picked = input("Pick a number: ")
    return number_picked

def echo_user_input(x):
    print(x)

def add_two_number(x,y):
    z =  int(x) + int(y)
    print(z)

def multiply_3_numbers(x,y,z):
    a = int(x) * int(y) * int(z)
    return(a)

def determine_largest(x,y):
    if int(x) < int(y):
        print(y + " is larger")
    if int(x) > int (y):
        print(x + " is larger")

a = ask_for_input()

echo_user_input(a)

a = ask_for_input()
b = ask_for_input()
add_two_number(a,b)

product = multiply_3_numbers(ask_for_input(),ask_for_input(),ask_for_input())
echo_user_input(product)

a = ask_for_input
b = ask_for_input
determine_largest(ask_for_input(),ask_for_input())# on
