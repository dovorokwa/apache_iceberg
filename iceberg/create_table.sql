
CREATE TABLE nyc_taxi_iceberg (
  vendor_id STRING,
  tpep_pickup_datetime TIMESTAMP,
  tpep_dropoff_datetime TIMESTAMP,
  passenger_count INT,
  trip_distance DOUBLE,
  fare_amount DOUBLE
)
PARTITIONED BY (pickup_date)
STORED AS ICEBERG
LOCATION 's3://nyc-taxi-iceberg-bucket/nyc_taxi_table';
