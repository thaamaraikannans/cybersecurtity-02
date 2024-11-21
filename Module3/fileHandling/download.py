import requests

url = "https://cdn4.gotofiles.online/download/1ad8a1e715cbc27ee529dde0beadef38/1732198116/p/Tamil%20HD%20Mobile%20Movies/Ra%20One%20(2011)/Ra%20One%20(Original)/Ra%20One%20(640x360)/Ra%20One%20HD%20Sample.mp4"
response = requests.get(url, stream=True)

with open("person.mp4", "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
        f.write(chunk)