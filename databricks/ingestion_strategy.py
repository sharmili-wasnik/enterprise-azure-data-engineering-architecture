from delta.tables import DeltaTable

def full_refresh(df, path):
    df.write.format("delta").mode("overwrite").save(path)

def append_load(df, path):
    df.write.format("delta").mode("append").save(path)

def upsert_load(df, path, condition):
    delta_table = DeltaTable.forPath(spark, path)

    delta_table.alias("target").merge(
        df.alias("source"),
        condition
    ).whenMatchedUpdateAll() \
     .whenNotMatchedInsertAll() \
     .execute()
