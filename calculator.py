def calculation(temp, windspeed):
    windchill = (35.74 + 0.6215 * temp) - 35.75 * (windspeed ** 0.16) + 0.4275 * temp * (windspeed ** 0.16)
    return windchill

def celfah(temp):
    temp = temp * (9/5) + 32
    return temp 

def user_input():
    temp = float(input("What is the temperature? "))
    f_c = input("Fahrenheit or Celsius (F/C)? ")
    return temp, f_c

temp, f_C = user_input()
windspeed = 5

#in case of the user input 'c' or 'f' instead of 'C' or 'F' I am utilizing the upper() function. So, won't have any issue to run even its lowcase. 
if f_C.upper() == "F":
    while windspeed < 65:
        win = calculation(temp, windspeed)
        print(f"At temperature {temp}F, and wind speed {windspeed} mph, the windchill is: {win:.2f}F")
        windspeed += 5
elif f_C.upper() == "C":
    temp = celfah(temp)
    while windspeed < 65:
        win = calculation(temp, windspeed)
        print(f"At temperature {temp}F, and wind speed {windspeed} mph, the windchill is: {win:.2f}F")
        windspeed += 5
else:
    quit()