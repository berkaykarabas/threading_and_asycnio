import threading
import requests
import time

def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et=time.time()
    elapsed_time = et-st
    print("Execution Time:", elapsed_time,"seconds")
    return json_array



class ThereadingDownloader(threading.Thread):

    json_array=()

    def __int__(self,url):
        super().__init__()
        self.url=url
    def run(self):
        response =requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array()
def get_data_threading(urls):
    st=time.time()
    threads=[]
    for url in urls:
        t = ThereadingDownloader(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
        print(t)
    et=time.time()
    elapsed_time=et-st
    print("Execution Time:", elapsed_time, "seconds")

urls = ["http://postman-echo.com/delay/3"] * 10
#get_data_sync(urls)
get_data_threading(urls)