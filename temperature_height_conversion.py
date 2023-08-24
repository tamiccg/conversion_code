TEMPERATURE = 1
HEIGHT = 2

heightOrTemperature = TEMPERATURE
while heightOrTemperature == TEMPERATURE or heightOrTemperature == HEIGHT:

    heightOrTemperature = int(
        input('What would you want to convert: 1- temperature or 2- height, another value- exit \n'))
    if heightOrTemperature == TEMPERATURE:
        direction = int(input('Direction for convert: 1- celsius for fahrenheit, 2- fahrenheit for celsius \n'))
        if direction == 1:
            convertCelsius = float(input('value to convert: \n'))
            resultFahrenheit = convertCelsius * 9 / 5 + 32
            print(f'the result of conversion is: {resultFahrenheit}')
        elif direction == 2:
            convertFahrenheit = float(input('value to convert: \n'))
            resultCelsius = (convertFahrenheit - 32) * 5 / 9
            print(f'the result of conversion is: {resultCelsius}')
    elif heightOrTemperature == HEIGHT:
        direction = int(input('Direction for convert: 1- cm for inches, 2- inches for cm \n'))
        if direction == 1:
            convertCm = float(input('value to convert: \n'))
            resultInches = convertCm / 2.54
            print(f'the result of conversion is: {resultInches:.4f}')
        elif direction == 2:
            convertInches = float(input('value to convert: \n'))
            resultCm = 2.54 * convertInches
            print(f'the result of conversion is: {resultCm}')
print(f'thank you for using our service')
