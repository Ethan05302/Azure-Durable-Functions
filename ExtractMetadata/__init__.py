import logging
import os
import json
from PIL import Image
from io import BytesIO
from azure.storage.blob import BlobServiceClient

def main(name: str) -> dict:
    logging.info(f"Extracting metadata from blob: {name}")

    # 修复路径前缀问题
    if "/" in name:
        name = name.split("/", 1)[1]

    connection_str = os.environ["AzureWebJobsStorage"]
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    container_client = blob_service_client.get_container_client("image-input")
    blob_client = container_client.get_blob_client(name)

    blob_data = blob_client.download_blob().readall()
    image = Image.open(BytesIO(blob_data))
    width, height = image.size
    image_format = image.format

    metadata = {
        "file_name": name,
        "file_size_kb": round(len(blob_data) / 1024, 2),
        "width": width,
        "height": height,
        "format": image_format
    }

    logging.info(f"Extracted metadata: {json.dumps(metadata)}")
    return metadata
