from pyspark.sql.functions import input_file_name, current_timestamp

def raw_to_foundation(raw_path, foundation_path, predefined_schema):

    df = spark.read.schema(predefined_schema).json(raw_path)

    df = df.withColumn("file_name", input_file_name()) \
           .withColumn("ingestion_time", current_timestamp())

    df.write.format("delta") \
        .mode("append") \
        .save(foundation_path)
