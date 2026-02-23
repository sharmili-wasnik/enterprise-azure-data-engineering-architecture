# Architecture

Raw Layer:
- Immutable storage from ADF copy activity

Foundation Layer:
- Schema enforced
- Append load
- Adds file_name & ingestion_time
- Stored as Delta

Enriched Layer:
- Business transformations
- Lookup joins
- Saved as Delta
