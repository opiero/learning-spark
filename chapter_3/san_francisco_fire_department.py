# In Python, define a schema
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct

# Create a SparkSession
spark = SparkSession.builder.appName("SanFranciscoFireDepartment").getOrCreate()

# Programmatic way to define a schema
fire_schema = StructType([StructField('CallNumber', IntegerType(), True),
                StructField('UnitID', StringType(), True),
                StructField('IncidentNumber', IntegerType(), True),
                StructField('CallType', StringType(), True),
                StructField('CallDate', StringType(), True),
                StructField('WatchDate', StringType(), True),
                StructField('CallFinalDisposition', StringType(), True),
                StructField('AvailableDtTm', StringType(), True),
                StructField('Address', StringType(), True),
                StructField('City', StringType(), True),
                StructField('Zipcode', IntegerType(), True),
                StructField('Battalion', StringType(), True),
                StructField('StationArea', StringType(), True),
                StructField('Box', StringType(), True),
                StructField('OriginalPriority', StringType(), True),
                StructField('Priority', StringType(), True),
                StructField('FinalPriority', IntegerType(), True),
                StructField('ALSUnit', BooleanType(), True),
                StructField('CallTypeGroup', StringType(), True),
                StructField('NumAlarms', IntegerType(), True),
                StructField('UnitType', StringType(), True),
                StructField('UnitSequenceInCallDispatch', IntegerType(), True),
                StructField('FirePreventionDistrict', StringType(), True),
                StructField('SupervisorDistrict', StringType(), True),
                StructField('Neighborhood', StringType(), True),
                StructField('Location', StringType(), True),
                StructField('RowID', StringType(), True),
                StructField('Delay', FloatType(), True)])

# Use the DataFrameReader interface to read a CSV file
sf_fire_file = "./sf-fire-calls.csv"
fire_df = spark.read.csv(sf_fire_file, header=True, schema=fire_schema)
#fire_df.write.format("parquet").save("./fire_calls.parquet")

# save as table
'''
parquet_table = "parquet_table"
fire_df.write.format("parquet").saveAsTable(parquet_table)
'''

#Projection (Filtering)
few_fire_df = fire_df \
    .select("IncidentNumber", "AvailableDtTm", "CallType") \
    .where(col("CallType") != "Medical Incident")


fire_df \
    .select("CallType") \
    .where( col("CallType").isNotNull() ) \
    .agg(countDistinct("CallType").alias("DistinctCallTypes"))\
    .show()

fire_df \
    .select("CallType") \
    .where(col("CallType").isNotNull()) \
    .distinct() \
    .show(10, False)
