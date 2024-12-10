
import org.apache.spark.sql.types._
 import org.apache.spark.sql._

val orders= Seq(
Row(1,"DP-203 Azure Data Engineer",10),
Row(2,"AZ-104 Azure Administrator",20),
Row(3,"DP-900 Azure Data Fundamentals",30))

val schema = StructType(Array(
 StructField("id", IntegerType,true),
 StructField("coursename", StringType,true),
 StructField("quantity", IntegerType,true)
))


val rdd = spark.sparkContext.parallelize(orders)
val df=spark.createDataFrame(rdd, schema)


df.show()

