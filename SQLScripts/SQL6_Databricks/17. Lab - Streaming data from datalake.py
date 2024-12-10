filePath="abfss://data@datalake7000.dfs.core.windows.net/csv/"

spark.conf.set(
  "fs.azure.account.key.datalake7000.dfs.core.windows.net",
  "ES5EbbZX68ooZmT3vuvoJ31KR0bOfNiTo8DVA7F39vJSPpNADN0yGOqgn+vqATQdPQFSVXRlk6eT+AStcnsu6Q=="
)

checkpoint="/tmp/checkpoint"
schemalocation="/tmp/schema"


rawdf = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schemalocation)
    .load(filePath)
)

display(rawdf)