import requests


def get_data_from_fastapi(endpoint, app):
    try:
        #app=App.get_running_app()
        BASE_URL = app.base_url
        response = requests.get(BASE_URL+endpoint)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data received from FastAPI server
            return data
        else:
            return 'error'
    except requests.exceptions.RequestException as e:
        return 'error'


def post_to_api(endpoint, payload, app):
    #app = App.get_running_app()
    BASE_URL = app.base_url
    response = requests.post(BASE_URL+endpoint, json=payload)
    if response.status_code == 200:
        print('POST request was successful!')
        print('Response:', response.text)
    else:
        print('POST request failed:', response.status_code)