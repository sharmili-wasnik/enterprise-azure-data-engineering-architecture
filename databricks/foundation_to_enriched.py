from pyspark.sql.functions import broadcast

def foundation_to_enriched(foundation_path, enriched_path, lookup_df):

    foundation_df = spark.read.format("delta").load(foundation_path)

    enriched_df = foundation_df.join(
        broadcast(lookup_df),
        foundation_df.id == lookup_df.source_id,
        "left"
    )

    enriched_df.write.format("delta") \
        .mode("overwrite") \
        .save(enriched_path)
