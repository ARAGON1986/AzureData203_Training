df = spark.read.load("abfss://data@datalake7000.dfs.core.windows.net/parquet/ActivityLog01.parquet", format="parquet")display(df.select("Operationname","Status","Resourcetype"))

df.count()

display(df.where(df['Resourcegroup']=="app-grp"))

filtereddf=df.where(df['Resourcegroup']=="app-grp")
filtereddf.count()

from pyspark.sql.functions import col
filtereddf=df.filter(col('Resourcegroup').isNotNull())
display(filtereddf)
