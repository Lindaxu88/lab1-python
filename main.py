#Author: Yeman Xu ybx5148@psu.edu
#Collaborator: Shiao Zhuang sqz5328@psu.edu
#Collaborator: Zhihong Jiang zbj5088@psu.edu

temperature = input ("Enter temperature: ")
Ftemperature = float(temperature)
unit = input("Enter unit in F/f or C/c: ")
if unit == "c" or unit == "C":
  print(str(temperature) + "°" + " in Celsius is equivalent to " + str(Ftemperature*1.8+32) + "°" + " Fahrenheit.")
elif unit == "f" or unit == "F":
  print(str(temperature) + "°" + " in Fahrenheit is equivalent to " + str((Ftemperature-32)*(5/9)) + "°" + " Celsius.")
else :
  print(f"Invalid unit({unit}).")
