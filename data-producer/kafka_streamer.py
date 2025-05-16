
from confluent_kafka import Producer
import pandas as pd
import json
import time

producer = Producer({
    'bootstrap.servers': 'your-broker',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'your-username',
    'sasl.password': 'your-password',
    'sasl.mechanisms': 'PLAIN'
})

df = pd.read_csv('../datasets/yellow_tripdata_2023-01.csv')

for _, row in df.iterrows():
    producer.produce('nyc-taxi-topic', value=row.to_json())
    time.sleep(0.05)

producer.flush()
