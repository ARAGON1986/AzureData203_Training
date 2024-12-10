// Lab - Spark Pool - Write data to Azure Synapse

import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._


val dataSchema = StructType(Array(    
    StructField("Correlationid", StringType, true),
    StructField("Operationname", StringType, true),
    StructField("Status", StringType, true),
    StructField("Eventcategory", StringType, true),
    StructField("Level", StringType, true),
    StructField("Time", TimestampType, true),
    StructField("Subscription", StringType, true),
    StructField("Eventinitiatedby", StringType, true),
    StructField("Resourcetype", StringType, true),
    StructField("Resourcegroup", StringType, true),
    StructField("Resource", StringType, true)))


val df = spark.read.format("csv").option("header","true").schema(dataSchema).load("abfss://data@datalake7000.dfs.core.windows.net/csv/ActivityLog01.csv")

val writeOptionsWithBasicAuth:Map[String, String] = Map(Constants.SERVER -> "dataworkspace50000.sql.azuresynapse.net",
                                           Constants.USER -> "sqladminuser",
                                           Constants.PASSWORD -> "Microsoft@123",
                                           Constants.DATA_SOURCE -> "datapool",                                    
                                           Constants.TEMP_FOLDER -> "abfss://staging@datalake7000.dfs.core.windows.net",
                                           Constants.STAGING_STORAGE_ACCOUNT_KEY -> "ES5EbbZX68ooZmT3vuvoJ31KR0bOfNiTo8DVA7F39vJSPpNADN0yGOqgn+vqATQdPQFSVXRlk6eT+AStcnsu6Q==")

import org.apache.spark.sql.SaveMode
import com.microsoft.spark.sqlanalytics.utils.Constants
import org.apache.spark.sql.SqlAnalyticsConnector._

df.
    write.    
    options(writeOptionsWithBasicAuth).
    mode(SaveMode.Overwrite).    
    synapsesql(tableName = "datapool.dbo.PoolActivityLog",                 
                tableType = Constants.INTERNAL,                 
                location = None
                )

