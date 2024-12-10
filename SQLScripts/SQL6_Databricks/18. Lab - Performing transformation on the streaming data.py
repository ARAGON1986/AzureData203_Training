
%sql
SELECT COUNT(*) FROM default.activitylogdata
filePath="abfss://data@datalake7000.dfs.core.windows.net/csv/"

filePath="abfss://data@datalake4000700.dfs.core.windows.net/csv/"

spark.conf.set(
  "fs.azure.account.key.datalake4000700.dfs.core.windows.net",
  "bCBgDDa2CdbZ3Jtdl2Rq4omVuO6+qNN+1xWGrJ86DJQUCMB4f1p01f1I9ifFswLeIdmYBaowny2A+AStjkDc+w=="
)

checkpoint="/tmp/checkpoint"
schemalocation="/tmp/schema"

rawdf=spark.readStream.format("cloudFiles").option("cloudFiles.format", "csv").option("cloudFiles.schemaLocation", schemalocation).load(filePath)

filtereddf=rawdf.filter(col('Resourcegroup').isNotNull())
filtereddf.writeStream.format("delta").outputMode("append").option("checkpointLocation", checkpoint).option("mergeSchema","true").table("default.activitylogdata")