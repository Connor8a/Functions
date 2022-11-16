# Conversion Calculator
# By: Connor Ochoa 

# Conversion of Length 
Length = int(input("Please enter a number: "))
print(Length)

# User input regarding the length to convert 
while (True):
    try:
     user_unit = input("What unit of measurement is your number (ex: inches): ")
    except:
        print("invalid input")
    else:
        if user_unit != "inches" or user_unit != "milimeters":
            print("invalid input")
        else:
            break

#to convert inches to milimeters --> in x 25.4
#to convert milimeters to inches --> mm / 25.4
#user gives in unit 
if user_unit == "inches":
    conv_number = Length * 25.4
    print(conv_number)
    conv_unit = 'mm'

if user_unit == "milimeters":
    conv_number2 = Length / 25.4
    print(conv_number2)
    conv_unit = 'in'




print(conv_number, conv_unit)

# Get the unit 

#convert the length to the correct unit 

# convert the length 

# Output the answer

# Graceful Conclusion 