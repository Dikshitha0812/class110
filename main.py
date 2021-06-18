import pandas
import statistics
import random

df=pandas.read_csv("data.csv")
print(df.head())
temp=df["temp"]
mean=statistics.mean(temp)
median=statistics.median(temp)
mode=statistics.mode(temp)
print(mean,median,mode)
#code tofind mean medianmode for 100 samplepoints
def experiment():
    ds=[]
    for i  in range  (0,100):
        index=random.randint(0,len(temp)-1)
        value=temp[index]
        ds.append(value)

    meanOfSample=statistics.mean(ds)
    return(meanOfSample)

meanSample=[]
def sampling():
  
    for i in range(0,1000):
        meaan1=experiment()
        meanSample.append(meaan1)

sampling()
samplingmeandistribution=statistics.mean(meanSample)

median2=statistics.median(meanSample)
mode2=statistics.mode(meanSample)
print(samplingmeandistribution,median2,mode2)