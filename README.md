
# NYC Taxi Streaming Data Lakehouse on AWS with Kafka, Glue & Iceberg

This project demonstrates an end-to-end streaming data pipeline using:

- **Confluent Kafka** for real-time ingestion
- **AWS Glue** for ETL
- **Apache Iceberg** for lakehouse table format

## Steps

1. Stream NYC taxi data to Kafka using Python
2. Use a Kafka sink connector to store raw data in S3
3. Run AWS Glue ETL to process and write data in Iceberg format
4. Query with Athena or Spark

## Setup

- Provision infrastructure using Terraform
- Stream sample CSV using `data-producer/kafka_streamer.py`
- Trigger the Glue job using `glue-job/glue_etl_script.py`
- Use `iceberg/create_table.sql` to create your Iceberg table
