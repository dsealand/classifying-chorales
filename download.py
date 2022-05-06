import requests
import sys

def download(url, composer, filename):
    print(url, composer, filename)

    r = requests.get(url, allow_redirects=True)

    filepath = composer + '/' + filename
    open(filepath, 'wb').write(r.content)


if __name__ == "__main__":
    download(sys.argv[1], sys.argv[2], sys.argv[3])