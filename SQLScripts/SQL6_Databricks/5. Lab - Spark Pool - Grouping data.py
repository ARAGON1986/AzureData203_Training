df = spark.read.load("abfss://data@datalake7000.dfs.core.windows.net/parquet/ActivityLog01.parquet", format="parquet")

from pyspark.sql.functions import col
filtereddf=df.filter(col('Resourcegroup').isNotNull())

summarydf=filtereddf.groupby('Resourcegroup').count()
display(summarydf)