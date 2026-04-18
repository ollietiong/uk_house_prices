import requests

def download_file(url:str, output_path:str):
    r = requests.get(url)
    r.raise_for_status()

    with open(output_path,"wb")as f:
        f.write(r.content)
