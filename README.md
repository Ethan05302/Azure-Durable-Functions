# Azure Durable Functions - Image Metadata Processing

## Project Description

This project demonstrates the use of Azure Durable Functions (Python) to implement an image metadata processing workflow. The goal is to automatically extract metadata from uploaded images and store it in an Azure SQL Database. This is achieved through a serverless architecture using Azure Functions, Blob Storage, Durable Orchestrator, and SQL binding.

## Functionality Overview

- When a new image is uploaded to Azure Blob Storage (`image-input` container), a Blob Trigger function is invoked.
- This function starts a Durable Orchestration.
- The orchestrator calls an activity function to extract metadata (file name, size, width, height, and format).
- The orchestrator then calls another activity function to store this metadata in the Azure SQL Database (`ImageMetadata` table).

## Project Structure

```
image-metadata-durable/
├── BlobTriggerClient/        # Starts orchestration on new blob
│   └── __init__.py
├── OrchestratorFunction/     # Coordinates activities
│   └── __init__.py
├── ExtractMetadata/          # Extracts image metadata
│   └── __init__.py
├── StoreMetadata/            # Stores metadata into Azure SQL
│   └── __init__.py
├── requirements.txt          # Python dependencies
├── host.json                 # Azure Functions host config
└── local.settings.json       # Local development settings (not uploaded)
```

## Required Services

- Azure Blob Storage
- Azure Durable Functions (Python v1)
- Azure SQL Database
- pyodbc and Pillow libraries

## Setup Instructions

1. Create Azure resources: Storage Account, SQL Server, and SQL Database.
2. Set up the `ImageMetadata` table in your SQL database:

```sql
CREATE TABLE ImageMetadata (
    file_name NVARCHAR(255),
    file_size_kb FLOAT,
    width INT,
    height INT,
    format NVARCHAR(50)
);
```

3. Configure `local.settings.json` with your SQL connection string and storage details.
4. Deploy the project using Visual Studio Code with the Azure Functions extension or via Azure CLI.
5. Upload an image to the `image-input` container.
6. Check the SQL database to confirm that metadata has been stored.

## Dependencies

Install required libraries using pip:

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes:

```
azure-functions
azure-storage-blob
Pillow
pyodbc
```

## Demo Video
https://youtu.be/MKBUR53flbQ
