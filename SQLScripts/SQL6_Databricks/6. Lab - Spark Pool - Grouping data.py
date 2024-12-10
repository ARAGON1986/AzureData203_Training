df = spark.read.load("abfss://data@datalake7000.dfs.core.windows.net/parquet/ActivityLog01.parquet", format="parquet")

tablepath="/delta/ActivityLog"
df.write.format("delta").save(tablepath)

ActivityLogdf = spark.read.format("delta").load(tablepath)
display(ActivityLogdf)



