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

filtereddf.writeStream.format("com.databricks.spark.sqldw") \
  .option("url", "jdbc:sqlserver://dataworkspace40040.sql.azuresynapse.net:1433;database=datapool") \
  .option("user","sqladminuser") \
  .option("password","Microsoft@123") \
  .option("tempDir", "abfss://staging@datalake4000700.dfs.core.windows.net/databricks") \
  .option("forwardSparkAzureStorageCredentials", "true") \
  .option("dbTable", "dbo.PoolActivityLog") \
  .option("checkpointLocation", checkpoint).start()