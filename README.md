#  Financial Trades Settlement Pipeline

##  Overview
Built a batch ELT pipeline for processing financial trade data and computing P&L using AWS services.

##  Architecture
Python → S3 → Glue Crawler → Athena → S3 (Processed) → QuickSight

##  Technologies
- Amazon S3
- AWS Glue (Crawler + Data Catalog)
- Amazon Athena
- Amazon QuickSight
- Python

##  Workflow
1. Generate trade data using Python
2. Upload data to S3 (raw zone)
3. Use Glue Crawler to infer schema
4. Query data using Athena
5. Transform data (P&L calculation)
6. Store processed data in S3
7. Visualize in QuickSight

##  Key Features
- Automated trade data ingestion
- ELT processing using Athena
- P&L calculation using SQL
- Serverless architecture
- Interactive dashboards

##  Outcome
- Built scalable financial data pipeline
- Processed trade data end-to-end
- Generated real-time analytics dashboards
