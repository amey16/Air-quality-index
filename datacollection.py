import os
import time
import requests
import sys

def retrieve_html():
    for year in range(1997,2021):
        for month in range(1,13):
            if(month<10):
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)
    
            source_text = requests.get(url)
            text_utf = source_text.text.encode('utf=8')

            if not os.path.exists("Data/html_Data/dl-sf/{}".format(year)):
                os.makedirs("Data/Html_Data/dl-sf/{}".format(year))
            with open("Data/Html_Data/dl-sf/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)

    for year in range(1997,2021):
        for month in range(1,13):
            if(month<10):
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-421810.html'.format(month,year)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-421810.html'.format(month,year)
    
            source_text = requests.get(url)
            text_utf = source_text.text.encode('utf=8')

            if not os.path.exists("Data/html_Data/dl-p/{}".format(year)):
                os.makedirs("Data/Html_Data/dl-p/{}".format(year))
            with open("Data/Html_Data/dl-p/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)

        sys.stdout.flush()

if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("time taken to web scrape: {}".format(stop_time-start_time))