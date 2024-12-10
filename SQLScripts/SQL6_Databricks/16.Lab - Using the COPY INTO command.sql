%sql
CREATE DATABASE appdb

%sql
USE appdb

%sql
CREATE TABLE logdata

%sql
COPY INTO logdata
FROM 'abfss://data@datalake4000700.dfs.core.windows.net/parquet/ActivityLog01.parquet'
FILEFORMAT = PARQUET
COPY_OPTIONS ('mergeSchema' = 'true')