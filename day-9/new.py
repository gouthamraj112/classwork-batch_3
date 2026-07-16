import requests

BASE_URL="https://jsonplaceholder.typicode.com/"

#GET -fetch a user
response=requests.get(f"{BASE_URL}/users/1")
print(response.status_code)
print(response.json())

#POST-create a new user
new_post={"title":"Hello","body":"world","user_id":50}
response=requests.post(f"{BASE_URL}/posts",json=new_post)
print(response.status_code)
print(response.json())
