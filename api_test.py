import requests

response = requests.get("https://api.github.com")

print(response.status_code)
data = response.json()

print(data["current_user_url"])
print(data["repository_url"])