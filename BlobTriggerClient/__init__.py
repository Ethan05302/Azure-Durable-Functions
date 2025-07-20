import logging
import azure.functions as func
import azure.durable_functions as df

async def main(myblob: func.InputStream, starter: str):
    logging.info(f"Blob trigger processed blob: {myblob.name}, size: {myblob.length} bytes")

    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("OrchestratorFunction", None, myblob.name)

    logging.info(f"Started orchestration with ID = '{instance_id}'")
