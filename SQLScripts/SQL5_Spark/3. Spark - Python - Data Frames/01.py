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

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("coursename",StringType(), True),
    StructField("quantity", IntegerType(), True)
])

orders= [
(1,"DP-203 Azure Data Engineer",10),
(2,"AZ-104 Azure Administrator",20),
(3,"DP-900 Azure Data Fundamentals",30)]

df = spark.createDataFrame(orders, schema)

df.show()