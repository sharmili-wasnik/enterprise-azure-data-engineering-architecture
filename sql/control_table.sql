CREATE TABLE ingestion_control (
    source_name VARCHAR(100),
    table_name VARCHAR(100),
    ingestion_type VARCHAR(20),
    watermark_column VARCHAR(100),
    last_watermark_value DATETIME,
    schema_definition NVARCHAR(MAX),
    target_path VARCHAR(200),
    is_active BIT
);
