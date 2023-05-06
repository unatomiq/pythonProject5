import json

import requests

base_url = 'https://petstore.swagger.io/v2/'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {
    "id": 0,
    "username": "test",
    "firstName": "test",
    "lastName": "test",
    "email": "test",
    "password": "test",
    "phone": "test",
    "userStatus": 0
}
updated_data = {
    "id": 0,
    "username": "test1",
    "firstName": "test1",
    "lastName": "test1",
    "email": "test1",
    "password": "test1",
    "phone": "test1",
    "userStatus": 0
}


def print_response(request):
    print(request.status_code)
    print(request.json())


post_res = requests.post(f"{base_url}user", headers=headers, data=json.dumps(data))
print_response(post_res)

get_res = requests.get(f"{base_url}user/login", headers=headers,
                       data={'username': data['username'], 'password': data['password']})
print_response(get_res)

put_res = requests.put(f"{base_url}user/test", headers=headers, data=json.dumps(updated_data))
print_response(put_res)

delete_res = requests.delete(f"{base_url}user/" + updated_data["username"], headers=headers)
print_response(delete_res)
