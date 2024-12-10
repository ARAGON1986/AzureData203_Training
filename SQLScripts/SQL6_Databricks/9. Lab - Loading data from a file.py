filePath="/FileStore/parquet/ActivityLog01.parquet"

df = spark.read.load(filePath, format="parquet")
display(df)