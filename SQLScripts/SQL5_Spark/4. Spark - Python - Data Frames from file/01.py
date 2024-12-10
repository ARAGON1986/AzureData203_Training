import findspark
findspark.init()
findspark.find()

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark=(
    SparkSession
    .builder
    .appName("DP203")
    .getOrCreate()
)
spark

df = spark.read.csv("D:\\data\orders.csv",
    header=True,
    inferSchema=True,
    sep=",")


df.show()