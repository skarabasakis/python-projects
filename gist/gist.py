import os
import sys
import json

import http.client # httplib
import urllib.request # urllib (higher-level that httplib)
import requests # nicer alternative to urllib, can be installed from pypi


token = os.getenv('GH_TOKEN')
if not token:
  raise RuntimeError("GH_TOKEN not set")

paths = sys.argv[1:]
if not paths:
  raise RuntimeError("No file paths specified")

files = {}
for path in paths:
  filename = os.path.basename(path)
  if not filename:
    raise RuntimeError(f"Not a file: {path}")

  with open(path, "r") as file:
     files[filename] = {"content": file.read()}

# Prepare request headers
headers = {
  'Authorization': f'Bearer {token}',
  'User-agent': 'python-gist',
  'Accept': 'application/json',
  'X-GitHub-Api-Version': '2022-11-28'
}

# Prepare request body
body = {
  "files": files
}

# Perform request
def create_gist_with_httplib(headers, body):
  connection = http.client.HTTPSConnection("api.github.com")
  connection.request("POST", "/gists", json.dumps(body), headers)
  response = connection.getresponse()
  if response.code == 201:
    response_data = json.loads(response.read())
    connection.close()
    return response_data["html_url"]
  else:
    status_code = response.code
    connection.close()
    raise RuntimeError(f"Github api error: {status_code}")


def create_gist_with_urllib(headers, body):
  response = urllib.request.urlopen(urllib.request.Request('https://api.github.com/gists', json.dumps(body).encode(), headers))
  if response.code == 201:
    response_data = json.loads(response.read())
    return response_data["html_url"]
  else:
    raise RuntimeError(f"Github api error: {response.code}")


def create_gist_with_requests(headers, body):
  response = requests.post('https://api.github.com/gists', json=body, headers=headers)
  if response.ok:
    response_data = response.json()
    return response_data["html_url"]
  else:
    raise RuntimeError(f"Github api error: {response.status_code}")

print(create_gist_with_urllib(headers, body))
