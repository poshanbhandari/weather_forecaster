
while True:
    import requests
    api_key = 'ddcf42916c446c8b49f079abc7ed4c29'

    city = input('\nEnter city name: ')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        temp = data['main']['temp']
        # desc = data['weather'][0]['description']
        desc = data['weather'][0]['description']
        print(f' \nTemperature in clesius: {round(temp - 273.15,2) } C')
        print(f'Temperature in fahrenheit: {round(temp * 9/5 - 459.67,2) } F')
        print(f'Description: {desc}\n')
        print ("Hit CTRL C to exit")
    else:
        print('Error fetching weather data, Exitting')
        exit()
