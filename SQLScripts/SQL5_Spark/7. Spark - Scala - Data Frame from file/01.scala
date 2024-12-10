val df=spark.read
.option("header", "true")
    .option("inferSchema", "true")
    .option("delimiter", ",")
    .csv("D:\\data\\orders.csv")

df.printSchema()

df.show()