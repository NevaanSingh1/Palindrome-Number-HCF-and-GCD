def user_input():
    
    pass

def binary_to_decimal():
    binary_str = input("Enter a binary number ")
    try:
        decimal = int(binary_str, 2)
        print("The decimal value is:", decimal)
    except ValueError:
        print("Invalid binary number. Please enter only 0s and 1s.")


binary_to_decimal()