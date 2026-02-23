CREATE TABLE ingestion_audit (
    table_name VARCHAR(100),
    ingestion_time DATETIME,
    records_processed INT,
    status VARCHAR(20)
);
