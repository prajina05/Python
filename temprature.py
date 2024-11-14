#temprature converted: celsius to ferhenhiet, frehenhiet to celsius
#ask user for temperature value and also for unit
# temperature_converter.py
class TemperatureConverter:
    def __init__(self, temp, unit):
        self.temp = temp
        self.unit = unit.upper()

    def convert(self):
        if self.unit == 'C':
            converted_temp = (self.temp * 9/5) + 32
            return f"{self.temp}°C is {converted_temp:.2f}°F"
        elif self.unit == 'F':
            converted_temp = (self.temp - 32) * 5/9
            return f"{self.temp}°F is {converted_temp:.2f}°C"
        else:
            return "Invalid unit! Please use 'C' for Celsius or 'F' for Fahrenheit."

# Example usage
temp_value = float(input("Enter the temperature: "))
unit_value = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
converter=TemperatureConverter(temp_value,unit_value)
result=converter.convert()
print(result)