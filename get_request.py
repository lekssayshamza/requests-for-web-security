import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params = {"userId": 1}
headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, params=params, headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Content-Type: {response.headers["Content-Type"]}')
print(f'Server: {response.headers.get("Server", "Not Provided")}')

data = response.json()

print(f'Number of posts: {len(data)}')
print(f'First Post Title: {data[0]["title"]}')
print(f'Response Length: {len(response.text)} characters')