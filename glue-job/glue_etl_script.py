
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import *

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.json("s3://nyc-taxi-raw-data-bucket/")
df_clean = df.withColumn("pickup_date", to_date("tpep_pickup_datetime")).filter("passenger_count > 0")

df_clean.write.format("iceberg") \
    .mode("overwrite") \
    .option("path", "s3://nyc-taxi-iceberg-bucket/nyc_taxi_table") \
    .saveAsTable("nyc_taxi_iceberg")
