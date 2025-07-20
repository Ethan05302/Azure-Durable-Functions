import azure.durable_functions as df

def main(context):
    return df.Orchestrator.create(orchestrator_function)(context)

def orchestrator_function(context):
    input_name = context.get_input()

    metadata = yield context.call_activity('ExtractMetadata', input_name)
    yield context.call_activity('StoreMetadata', metadata)

    return metadata
