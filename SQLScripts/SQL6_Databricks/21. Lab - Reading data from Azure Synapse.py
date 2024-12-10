logdf=spark.read.format("com.databricks.spark.sqldw"). \
    option("url","jdbc:sqlserver://dataworkspace40040.sql.azuresynapse.net;database=datapool") \
    .option("user","sqladminuser").option("password","Microsoft@123") \
    .option("tempDir", "abfss://staging@datalake4000700.dfs.core.windows.net/databricks") \
    .option("forwardSparkAzureStorageCredentials", "true") \
    .option("query","SELECT * FROM dbo.VehicleTollBooth") \
    .load()

display(logdf)