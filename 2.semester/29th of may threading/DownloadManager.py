import requests,threading
def download_file(url):
    response = requests.get(url)
    filename = url.split("/")[-1] # Extract the filename from the URL
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

class ThreadedDownloading(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
    def download_file(self):
        response = requests.get(self.url)
        filename = self.url.split("/")[-1] # Extract the filename from the URL
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
D1 = ThreadedDownloading("https://static.lsm.lv/media/2021/02/large/1/eoe0.jpg")
D2 = ThreadedDownloading("https://static.lsm.lv/media/2024/05/large/1/nt62.jpg")

D1.download_file()
D2.download_file()