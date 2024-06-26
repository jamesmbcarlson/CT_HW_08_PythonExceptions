# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 8 Assignment: Python Exception Handling

### 1. Exceptional Weather Forecast

#convert temperature to celsius and catch any exceptions
def convert_from_f_to_c(temp_fahrenheit):
    try:
        temp_celsius = (temp_fahrenheit - 32) * 5/9
    except ZeroDivisionError:
        print("Error! Division by zero was attempted.")
    except OverflowError:
        print("An overflow error has occured.")
    except Exception as e:
        print("An error has occured:", e)
    else:
        print(f"{temp_fahrenheit}°F converted to Celsisus: {round(temp_celsius, 2)}°C")
    finally:
        print("Thank you for using the Weather Forecast Application™!")
    
while True:
    # get input and check validity
    temp_input = input("Enter the Farenheit temperature you would like to convert to Celsius: ")
    try:
        temp = float(temp_input)
    except ValueError:
        print("Input can only be a number. Please try again.")
    else:
        convert_from_f_to_c(temp)
        break