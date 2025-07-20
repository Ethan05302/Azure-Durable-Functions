import logging
import pyodbc
import json

def main(metadata: dict) -> None:
    logging.info(f"[INFO] Storing metadata: {metadata}")

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=imagemetadata-sql-1234.database.windows.net;"
        "DATABASE=ImageDB;"
        "UID=sqladminuser;"
        "PWD=200530Zz.;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ImageMetadata (file_name, file_size_kb, width, height, format)
        VALUES (?, ?, ?, ?, ?)
    """, (
        metadata["file_name"],
        metadata["file_size_kb"],
        metadata["width"],
        metadata["height"],
        metadata["format"]
    ))
    conn.commit()
    cursor.close()
    conn.close()
