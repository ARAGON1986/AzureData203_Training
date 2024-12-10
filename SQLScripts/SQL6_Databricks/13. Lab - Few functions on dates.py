

from pyspark.sql.types import StructType,StringType,TimestampType

filePath="abfss://data@datalake4000700.dfs.core.windows.net/csv/ActivityLog01.csv"

spark.conf.set(
  "fs.azure.account.key.datalake4000700.dfs.core.windows.net",
  "bCBgDDa2CdbZ3Jtdl2Rq4omVuO6+qNN+1xWGrJ86DJQUCMB4f1p01f1I9ifFswLeIdmYBaowny2A+AStjkDc+w=="
)
dataSchema = StructType() \
    .add("Correlationid", StringType(), True) \
    .add("Operationname", StringType(), True) \
    .add("Status", StringType(), True) \
    .add("Eventcategory",StringType(), True) \
    .add("Level",StringType(),True) \
    .add("Time", TimestampType(), True) \
    .add("Subscription",StringType(), True) \
    .add("Eventinitiatedby", StringType(), True) \
    .add("Resourcetype",StringType(),True) \
    .add("Resourcegroup",StringType(),True) \
    .add("Resource",StringType(),True)

df = spark.read.format("csv").option("header",True).schema(dataSchema).load(filePath)  
display(df)


from pyspark.sql.functions import year,month,dayofyear
display(df.select(year(col("Time")).alias("Year"),month(col("Time")).alias("Month"),dayofyear(col("Time")).alias("Day of year")))

from pyspark.sql.functions import to_date
display(df.select(to_date(col("Time"),"dd-mm-yyyy").alias("Date")))