filePath="abfss://data@datalake7000.dfs.core.windows.net/parquet/ActivityLog01.parquet"

spark.conf.set(
  "fs.azure.account.key.datalake7000.dfs.core.windows.net",
  "ES5EbbZX68ooZmT3vuvoJ31KR0bOfNiTo8DVA7F39vJSPpNADN0yGOqgn+vqATQdPQFSVXRlk6eT+AStcnsu6Q=="
)

df = spark.read.load(filePath,format="parquet")
                   
display(df)


---------------------


display(df.where(df['Resourcegroup']=="app-grp"))


---------------------

from pyspark.sql.functions import col
filtereddf=df.filter(col('Resourcegroup').isNotNull())
display(filtereddf)