from pyspark.sql.functions import col

def get_incremental_data(df, watermark_column, last_watermark):
    return df.filter(col(watermark_column) > last_watermark)
