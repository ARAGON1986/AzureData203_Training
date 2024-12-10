from pyspark.sql.types import StructType,StringType,TimestampType

filePath="abfss://data@datalake4000700.dfs.core.windows.net/json/customer_obj.json"

spark.conf.set(
  "fs.azure.account.key.datalake4000700.dfs.core.windows.net",
  "bCBgDDa2CdbZ3Jtdl2Rq4omVuO6+qNN+1xWGrJ86DJQUCMB4f1p01f1I9ifFswLeIdmYBaowny2A+AStjkDc+w=="
)

df = spark.read.format("json").load(filePath)  
display(df)

from pyspark.sql.functions import explode
explodeddf=df.select(col("customerid"),col("customername"),explode(col("courses")))
display(explodeddf)

from pyspark.sql.functions import explode
explodeddf=df.select(col("customerid"),col("customername"),explode(col("courses")),col("details.city"),col("details.mobile"))
display(explodeddf)

Adding an alias for the column name in the output
from pyspark.sql.functions import explode
explodeddf=df.select(col("customerid"),col("customername"),explode(col("courses")).alias("coursename"),col("details.city"),col("details.mobile"))
display(explodeddf)

