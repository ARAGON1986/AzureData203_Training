%scala

val filePath="abfss://data@datalake7000.dfs.core.windows.net/parquet/ActivityLog01.parquet"

spark.conf.set(
  "fs.azure.account.key.datalake7000.dfs.core.windows.net",
  "ES5EbbZX68ooZmT3vuvoJ31KR0bOfNiTo8DVA7F39vJSPpNADN0yGOqgn+vqATQdPQFSVXRlk6eT+AStcnsu6Q=="
)

val df = spark.read.format("parquet").load(filePath)
                   
display(df)