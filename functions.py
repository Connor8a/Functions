# Conversion Calculator
# By: Connor Ochoa 

# Conversion of Length 
def user_parcer(Length, user_unit):
    print('I will parse your data')
    # figure out a way to seperate the number from unit
    values = Length.rsplit(" ")
    print (values)



while(True):
    try:
        Length = float(input("Please enter a number: "))
        # Length = input("number and unit to convert: ")
        #if Length.isdigit():
        #   user_number = float (user_number)
        #   break
        #else:
        #   print("please use a number")
    except:
        print("invalid input")
    else:
        break
print(Length)

# User input regarding the length to convert 
while (True):
    try:
     user_unit = input("What unit of measurement is your number (ex: inches): ")
    except:
        print("invalid input")
    else:
        if user_unit == "inches" or user_unit == "milimeters":
            break
        else:
            print("invalid input")

#to convert inches to milimeters --> in x 25.4
#to convert milimeters to inches --> mm / 25.4
#user gives in unit 
if user_unit == "inches":
    conv_number = Length * 25.4
    print(conv_number)
    conv_unit = 'in'

if user_unit == "milimeters":
    conv_number2 = Length / 25.4
    print(conv_number2)
    conv_unit = 'mm'



print(conv_number, conv_unit)

# Get the unit 

#convert the length to the correct unit 

# convert the length 

# Output the answer

# Graceful Conclusion 