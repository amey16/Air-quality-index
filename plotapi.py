import pandas as pd
import matplotlib.pyplot as plt

def avg_data(year):
    average=[]
    for rows in pd.read_csv('Data/aqi/aqi{}.csv'.format(year),chunksize=24):
        temp=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                temp+=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    c=float(i)
                    temp+=c
        avg=temp/24
        average.append(avg)
    #print(len(average))
    return average

if __name__ == "__main__":
    lst2013 = avg_data(2013)
    lst2014 = avg_data(2014)
    lst2015 = avg_data(2015)
    lst2016 = avg_data(2016)
    lst2017 = avg_data(2017)
    lst2018 = avg_data(2018)
    plt.plot(range(0,365),lst2013,label = "2013 data")
    plt.plot(range(0,364),lst2014,label = "2014 data")
    plt.plot(range(0,365),lst2015,label = "2015 data")
    plt.plot(range(0,121),lst2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()

