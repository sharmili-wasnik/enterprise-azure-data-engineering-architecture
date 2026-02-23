def repartition_df(df, column_name):
    return df.repartition(column_name)

def optimize_table(path):
    spark.sql(f"OPTIMIZE delta.`{path}`")

def vacuum_table(path):
    spark.sql(f"VACUUM delta.`{path}` RETAIN 168 HOURS")
