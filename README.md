# Azure End-to-End Data Ingestion Pipeline

Enterprise-grade metadata-driven Azure data engineering framework implementing Medallion Architecture (Raw → Foundation → Enriched).

## Services Used
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure SQL Database
- Azure Databricks (Delta Lake)

## Features
- FULL / APPEND / INCREMENTAL / UPSERT ingestion
- Watermark-driven incremental loading
- Delta Lake MERGE operations
- Broadcast joins & skew mitigation
- Metadata-driven architecture
- OOM prevention techniques

## Architecture
Source → ADF → Raw (ADLS) → Databricks → Foundation (Delta) → Enriched (Delta) → BI / ML
