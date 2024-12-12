# AzureData203_Training
SQL sets for data 203 in Azure
# DATA WAREHOUSE

## INTRODUCTION OF CONCEPTS

**Warehouse**
A warehouse filled with data. Not the same as a database.  
Data inside of datawarehouse comes from elsewhere.

Data is copied not moved. There are rules that govern how to store the data.

> Rules
> - Integrated Environment: Multiple data sources 
> - Subject oriented
> - Time variant: contains historical data
> - Non volatile: remains stable in between refreshes

**Why DataWarehouse**
- Data driven decisions for past, present and future.
- One stop shopping for all the data.
- View into the unknown.

## BigData

**3V**
- Volume
- Velocity
- Variety

Semi structure and unstructure data using blob data types. Usually stored in data lakes.

## DATA WAREHOUSING ENVIRONMENT 

Data sources -> ETL/ELT -> Data Warehouse -> ETL/ELT -> Data Marts

Analogy with demand supply  
Supplier -> Wholesaler -> Retailers

## DATA WAREHOUSE ARCHITECHTURE

### CENTRALIZED DATA WAREHOUSE 

All sources come to the same single database.  
Support for one stop shopping.  
It is not easy to implement due to technology challenges, Work processes, human factors.  

### DATA MART 

Data warehouse is not the end point. Send further down stream into data marts.  
- Dependent Data Mart: Their existence depends on the data warehouse. 
- Independent Data Mart: Draw data from sources.

### ARCHITECHTURE

| Centralized                | Component Based        |
| :--------------------------- | :--------------------- |
| **EDW**                      | **Architechted**       | 
| 	Relational/Specialized     | 	DW + DM / DM        | 
| **DataLake**                 | 	Dependent           | 
| 	Hadoop/AWS S3              | 	Front-End DMs       | 
|                              | **Non Architechted**   | 
|                              | 	Federated EDW       | 

### CUBES

Cubes are multidimensional database 
- Fast query response time
- Good for "Modest" data volumes 100 Gb
- Less flexible than RDBMS

### OPERATIONAL DATA STORE 

ODS integrates multiple data into a single db but focuses on operational data 
Focuses on the current state of data integrated from different places

### STAGING LAYER

Every DWH needs a staging layer. Staging layer is landing zone for the data. 
Inside the staging layer create mirror images of the source. 
Many to 1 feeds if same software. 1 to 1 feeds in case of multiple source applications.

- Non persistent staging layer: Data is deleted after load to DWH.
- Persistent staging layer : Data stays in staging layer.

### ETL // ELT

ELT: 
- blast data into big data environment.
- Raw form in HDFS, AWS S3, Hadoop 
- Use big data env to transform
- Schema on read vs Schema on write

ETL:
1. Initial ETL: one time only
2. Incremental ETL: Refreshes DWH

ETL Patterns
- Append
- In-pace update
- Complete replacement
- Rolling append

### DATA TRANSFORMATION

Uniformity is important for Analytics
Restructuring the data

Transformation models
- Data value unification
- Data type and size unification
- De-duplication
- Dropping columns
- Value-based row filtering
- Correcting known errors
	
## DESIGN ENGINEERING OF DATA WAREHOUSE  

| BI Category                  | Data Model             |
| :--------------------------- | :--------------------- |
| Basic reporting              | Dimensional            | 
| OLAP                         | Dimensional            | 
| Predictive analytics         | Data Mining/specialized| 
| Exploratory analytics        | Data Mining/specialized| 

### PRINCIPLES OF DIMENSIONALITY

For every measurement need to have enough context
words *by* (sliced and grouped values) and *for* (specific value from dimension)
average annual salary *for assistant professor*, *by rank* 

FACTS 
- Additive: ex. credits
- Non Additive: ex. ratios, averages. Store underlying components.
- Semi Additive  

## STAR SCHEMA VS SNOWFLAKE SCHEMA 

OLAP: Dimensional Analysis of data. 
- Star Schema:  
All dimensions of a hierarchy is in one dimensional table.
Fewer database joins. PK and FK relations are straightforward. More storage needed. Denormalized dimension table.
- Snowflake schema:  
Each dimension level is in its own table. 
More joins. PK and FK relations are more complex. Less DB storage. Normalized dimension table.

## KEYS
- Primary Key: Unique identifier for each row. One or more columns.
- Foreign key: Some other table's primary key. Indicate logical relationships. 
- Natural key: travel from source sustem with the rest of the data. Aren't generated.
- Surrogate key: Use surrogate keys to relate data. No business meaning. Generated to relate the data.

Don't use natural keys. Use surrogate keys created in DWH instead. Keep natural keys as secondary keys. Discard natural keys in fact table.

Hierarchical vs. flat dimensions 

## TYPES OF FACT TABLES

- Transaction fact table:  
Record facts from transactions. 
Rules of fact tables:
Facts are available at the same grain -> look at the dimension, same dimension tables
Facts occurs simultaneously

- Periodic snapshot fact table  
Track a given measurement at regular intervals.
See aggregated transactions at a regular interval. 
Easier direct access for certain types of biz questions. 
Related to transaction fact tables or not related to transaction fact tables. 

- Accumulating snapshot fact table:
Track progress of biz process through stages.
Five different key to key relationships on same dimension table. 
Values accumulate as time passes by. 

- Factless fact table:  
Occurence of transaction without measurements.
An event we want to track but no measurement for that event. 
Multiple factless fact tables in same schema OK. 
Combine factless and transaction grain fact tables in same schema. 

Record a relationship among multiple parties even without transactions. 

## SQL for Dimension and Fact Tables

Need to specify primary key for dimension tables in star schema
Need to specify primary and foreign keys for snowflake schema 

In fact table primary keys are combinations of foreign keys in dim tables.

## SCD SLOWLY CHANGING DIMENSIONS

Techinques to manage history in DWH 

POLICIES 

- Type 1 Overwrite old data  
In-place update ETL pattern.

- Type 2 Maintain unlimited history  
Create new dimension row for each new version of history.

- Type 3 Maintain limited history
Small number of dimension table column for multiple versions of history.

## ETL DESIGN

Change data Capture
Limit the operations of incoming data to be processed. 
Process dimension tables before fact tables. 
Use:
- Timestamps
- Database logs
- database scan and compare

Steps:
Process Dimension Tables
1. data preparation
2. data transformation
3. process new dimension rows
4. process SCD type 1
5. process SCD type 2

Process Fact Tables

# AZURE DP-203
# DATA ENGINEERING WITH AZURE

## DESIGN AND IMPLEMENT DATA STORAGE

### DATA FORMATS

Data can be stored in many different ways.
- Structured: CSV, SQL DB
- Semi-Structured: JSON, XML 
- Unstructured: Images, Recordings

## AZURE DATA STORAGE SERVICES

- Blob Storage
- Storage azure files
- Storage queue
- Table Storage
- Azure SQL DB

## AZURE SYNAPSE ANALYTICS

Provide features to manage data.

- Synapse SQL
- Apache Spark for Azure SYNAPSE
- Data Integration: like data Factory and so

Need to create a workspace to work with Azure Synapse. 
Also need to have a lake gen 2 account for the workspace. 

### SERVERLESS SQL POOL

Allows to query data in azure datalake storage accout. .txt, parquet, .json.
The compute is managed for you. Only charged for data processed 5 USD for TB.

### SQL SERVER POOL

Create external tables. host sql DW.
Polybase access data in a data store like an Azure account. 

There is a control node that receives queries and sends them to different compute nodes.
Compute nodes and storage nodes are separate. 

**Hash-distributed tables**
For big tables like fact tables. Effective for handling a lot of data in read operations.

**Round-Robin tables**
Effective for loading data into staging tables. Data is evenly distributed across all distributions.
Default distribution when not defined.
Use for fact tables in DW

**Replicated tables**
Use for dimension tables in DW.

**index**
Automatically indexed by cluster
Less efficient for transient data
For transient data you can use HEAP table WITH (HEAP);

Define columns for cluster index WITH (CLUSTER INDEX(id));

## COPY DATA 

- Copy command: Go to control node first.
- Polybase: All data movement go to compute node in paralel. Better loading time.
- Bulk insert: Slower, simpler.

## TABLE PARTITION

Partitions are created on the date column. Supported for all distribution types.
Partition No recommended is 

**Partition Switch**
Move bulk of data based on partition. Partitions are done by date.
Usefull for deletion operations. 

## PIPELINES

Cache sink: store temporary data in cache env. Availble by default in the spark cluster.

## AZURE EVENT HUBS

Stream and ingest data service at a fast pace.

Event sources are streamed onto Azure Event Hubs. Data is ingested and sent to other service for processing.
Processing data can be done in Azure Stream Analytics or Azure Databricks.

In a hub you can create multiple partitions. Helps ingest more data at high speeds.

Billed based on throughput unit, is 1000 events per seconds in, 4096 events out.

Has the policy on shared access policies.

## AZURE STREAM ANALYTICS

Deliver data to different destination data stores. Take ingested data process in real time and send to data store.
Uses the policy on shared access policies.

Storage account in place to connect to Azure Synapse as a staging location.

Define Input, Output, Query and then start job. Timing is important for streaming.

**WINDOW FUNCTIONS**
Tumbling Window: Time window  
Hopping Window: time for data ingestion and calculations
Sliding Window: Criteria window

For complex nested JSON strutures use different stages in SQL query to get layers separately. With stage# AS SELECT QUERY
## NSG

flow logs to get incoming and outcoming traffic.

## SPARK

Hadoop was used to process big data. After that came Spark.
Spark is used to process data by doing transformations. Works with data in memory. Can use variety of Languages.
It takes data performs transformations and stores it in a data store.

## SPARK

Using spark within Azure synapse by implementing a spark pool.

## AZURE DATABRICKS

Having a data lakehouse in place. 
Databricks needs a workspace to store databricks assets.
Needs compute and job clusters to run. 

Need to create cluster in workspace 

## SECURITY

### COLUMN SECURITY ON AZURE SYNAPSE

CREATE USER userA WITHOUT LOGIN
GRANT SELECT ON [table](columns) TO userA
EXECUTE AS USER = 'UserA';

**Row level security**
Need to create a function to evaluate the value of a particular column.

CREATE SCHEMA security;
CREATE FUNCTION security.securitypredicate(@Agent AS nvarchar(50))
	RETURNS Table
WITH SCHEMABINDING
AS
	RETURN SELECT 1 AS securitypredicate_result
	WHERE @Agent = USER_NAME() OR USER_NAME() = 'Supervisor';

Need to create a policy to attach function to table 

CREATE SECURITY POLICY Filter
ADD FILTER PREDICATE Security.securitypredicate(Agent)
ON Tablename
WITH (STATE = ON);
GO

Finally grant security to users
GRANT SELECT ON Security.securitypredicate TO user;

### DYNAMIC DATA MASKING

Limits sensitive data disclosure by masking it to users. 
Define rules and functions for this.

### MASK DATA

Go to DB/security and add mask to desired column. 
Only applicable to non priviledge users. 

### ENCRYPTION OF DATA

Data is stored in disk in Azure storage. 
Encryption at rest through transparent data encryption. 

Azure key Vault: Stores the encryption key. Can only be done when creating the Synapse workspace.
Create key vault, give access to azure account with role assignment, crypto officer. Then create key.

### INTEGRATION OF ENTRA ID AND SYNAPSE

Storage Account is a public service. To access within VN only use VN SERVICE ENDPOINTS.

### MANAGED IDENTITES

Azure DataLake storage account connections by default uses account key.
A more secure approach is by the use of managed identity. 

### DATA DISCOVERY AND CLASSIFICATION

Available in Azure SQL and Synapse workspace. Used when it comes to accessing classified info.
To check who is accessing which data need to enable security/SQL auditing

## MICROSOFT PURVIEW

Data governance and compliance tool for Azure.
Discover data assets, maintain a data map, data catalog to understand the data lineage of data assets.

## NOTE ON FILE FORMATS

Parquet and ORC format is better when there are more read operations, focus on subset of columns.

Avro file is ideal for write transactions and need to fetch entire row info.

## ACCESS TIERS

Mechanism to reduce cost for data storage. 
Can change hot, cool, cold, Archive tiers for containers and blobs.
Under data management, life cycle management rules can move the data to different tiers or delete it.

## MONITOR

Allows to check the logs for all resources, get metrics and set up alerts.

## LOG ANALYTICS WORKSPACE

For logs of activities that need to be retained longer than 45 days.
Direct all logs to workspace to analyze the data later.

