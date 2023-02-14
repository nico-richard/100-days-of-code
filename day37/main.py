import requests

endpoint = "https://pixe.la/v1/"

# CREATE USER
body1 = {
    "token": "azertyazerty",
    "username": "nicolas-richard42",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(f"{endpoint}users", json=body1)
# print(response.content)

# CREATE GRAPH
body2 = {
    "id": "graph1",
    "name": "bike",
    "unit": "kilometers",
    "type": "float",
    "color": "shibafu"
}
# response = requests.post(f"{endpoint}users/nicolas-richard42/graphs",
#                          headers={"X-USER-TOKEN": "azertyazerty"}, json=body2)
# print(response.content)

# POST VALUE TO GRAPH
body3 = {
    "date": "20230211",
    "quantity": "3"
}
response = requests.post(f"{endpoint}users/nicolas-richard42/graphs/graph1",
                         headers={"X-USER-TOKEN": "azertyazerty"}, json=body3)
print(response.content)
