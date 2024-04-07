import requests

BASE_URL='http://127.0.0.1:8000'
ENDPOINT='/sen1'
def get_data_from_fastapi():
    try:
        response = requests.get(BASE_URL+ENDPOINT)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data received from FastAPI server
            print("Data received:", data)
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Call the function to get data from FastAPI server
get_data_from_fastapi()