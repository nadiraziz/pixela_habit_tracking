import requests


PIXELA_ENDPOINT = "https://pixe.la/v1/users"

TOKEN = "ASNF53jdf8s930sjs84j4"
USERNAME = "nadir"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": "graph2",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

graph_id = graph_params["id"]
ADD_PIXEL = f"{GRAPH_ENDPOINT}/{graph_id}"

add_pixel_params = {
    "date": "20210425",
    "quantity": "10.57"
}

response = requests.post(url=ADD_PIXEL, json=add_pixel_params, headers=headers)
print(response.text)