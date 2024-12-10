%scala
import org.apache.spark.eventhubs._

val eventHubConnectionString = ConnectionStringBuilder("Endpoint=sb://datahubnamespace200000.servicebus.windows.net/;SharedAccessKeyName=Eventhubpolicy;SharedAccessKey=QoSVnZRrXhB8YSycNYcOss85HTsxTRjYF+AEhMn986w=;EntityPath=datahub").build

val eventHubConfiguration = EventHubsConf(eventHubConnectionString) 

val eventhubDF=spark.readStream.format("eventhubs").options(eventHubConfiguration.toMap).load()

%scala
display(webhubDF)

=================================

Let's start from the begginig of the stream
%scala
import org.apache.spark.eventhubs._

val eventHubConnectionString = ConnectionStringBuilder("Endpoint=sb://datahubnamespace200000.servicebus.windows.net/;SharedAccessKeyName=Eventhubpolicy;SharedAccessKey=QoSVnZRrXhB8YSycNYcOss85HTsxTRjYF+AEhMn986w=;EntityPath=datahub").build

val eventHubConfiguration = EventHubsConf(eventHubConnectionString).setStartingPosition(EventPosition.fromStartOfStream)

val eventhubDF=spark.readStream.format("eventhubs").options(eventHubConfiguration.toMap).load()

%scala
display(eventhubDF.select(eventhubDF("body").cast("string")))

======================================
Now let's try to get the data 

We will define a structure for our data and we can get our data as a json object
%scala
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
val dataSchema = new StructType()
        .add("EntryTime", DataTypes.DateType)
        .add("CarModel", new StructType().add("Make",StringType).add("Model",StringType).add("VehicleType",IntegerType).add("VehicleWeight",IntegerType))
        .add("State", StringType)
        .add("TollAmount", IntegerType)
        .add("Tag", StringType)
        .add("TollId", IntegerType)
        .add("LicensePlate", StringType)
        .add("EventProcessedUtcTime", DataTypes.DateType)
        .add("PartitionId", IntegerType)
        .add("EventEnqueuedUtcTime", DataTypes.DateType)

val tmpDF=eventhubDF.select(eventhubDF("body").cast("string"))

val jsonDF=tmpDF.withColumn("body",from_json(col("body"),dataSchema))

display(jsonDF)

=====================================

If we want to display each element seperately

%scala
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
val dataSchema = new StructType()
        .add("EntryTime", DataTypes.DateType)
        .add("CarModel", new StructType().add("Make",StringType).add("Model",StringType).add("VehicleType",IntegerType).add("VehicleWeight",IntegerType))
        .add("State", StringType)
        .add("TollAmount", IntegerType)
        .add("Tag", StringType)
        .add("TollId", IntegerType)
        .add("LicensePlate", StringType)
        .add("EventProcessedUtcTime", DataTypes.DateType)
        .add("PartitionId", IntegerType)
        .add("EventEnqueuedUtcTime", DataTypes.DateType)

val tmpDF=eventhubDF.select(eventhubDF("body").cast("string"))

val jsonDF=tmpDF.withColumn("body",from_json(col("body"),dataSchema))

display(jsonDF.select("body.CarModel.Make","body.CarModel.Model","body.State","body.TollAmount"))

