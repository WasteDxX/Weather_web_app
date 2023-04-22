import requests
api_key='b0f244c5bd42880256a19a5252b9d119'
r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Dnipro&appid={api_key}&units=metric&lang=UA', auth=('user', 'pass'))
r_json = r.json()
temp=r_json['main']['temp']
weather_status=r_json["weather"][0]['main']
weather_img = '/Image/'+weather_status + '.png'