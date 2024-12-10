%sql
DROP TABLE default.activitylogdata


CREATE TABLE default.activitylogdata
(
   Correlationid STRING,
   Operationname STRING,
   Status STRING,
   Eventcategory STRING,
   Level STRING,
   Time TIMESTAMP,
   Subscription STRING,
   Eventinitiatedby STRING,
   Resourcetype STRING,
   Resourcegroup STRING,
   Resource STRING
)


filePath="abfss://data@datalake4000700.dfs.core.windows.net/csv/"

spark.conf.set(
  "fs.azure.account.key.datalake4000700.dfs.core.windows.net",
  "bCBgDDa2CdbZ3Jtdl2Rq4omVuO6+qNN+1xWGrJ86DJQUCMB4f1p01f1I9ifFswLeIdmYBaowny2A+AStjkDc+w=="
)

checkpoint="/tmp/checkpoint"
schemalocation="/tmp/schema"

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

rawdf=spark.readStream.format("cloudFiles").schema(dataSchema).option("cloudFiles.format", "csv").option("cloudFiles.schemaLocation", schemalocation).load(filePath)

filtereddf=rawdf.filter(col('Resourcegroup').isNotNull())
filtereddf.writeStream.format("delta").outputMode("append").option("checkpointLocation", checkpoint).option("mergeSchema","true").table("default.activitylogdata")