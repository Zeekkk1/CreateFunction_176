print ("Temperature Converter")
input_value = float(input("Enter the temperature value: "))
input_unit = input("Enter the unit (Celsius/Fahrenheit): ")


def ConvertTemperature ( Value, unit ) :
   if  unit == "Celsius":
       return (Value * 9/5) + 32
   elif unit == "Fahrenheit":
       return (Value - 32) * 5/9
   else:
       return "Invalid unit"

output_value = ConvertTemperature (input_value, input_unit)
print(f"The converted temperature is: {output_value}")