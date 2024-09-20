#import pandas as pd
#data_1=pd.read_csv('D:\SampleData\Input\Country.csv')
#print(data_1.shape)
#print(data_1.head(2))
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
#df = spark.read.csv('Country.csv',header=True,sep=',')
#df = spark.read.csv('Country.csv',header=True,inferSchema = True)
#df = spark.read.csv('Country.csv',header=True,inferSchema = True)
df = spark.read.csv('Country.csv',nullValue='NA',header=True,inferSchema = True)
df.printSchema()
df.show()
print(df.count())
df.show(2)
df.select('Name','age').show(2)