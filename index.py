import asyncio, logging, os
import json
from pyzeebe import ZeebeWorker, Job, create_insecure_channel

logging.basicConfig(format='%(levelname)s:%(message)s', 
    level=int(os.environ.get("LOGGING_LEVEL", "20")))


channel = create_insecure_channel(hostname=os.environ.get("HOSTNAME","localhost"), 
                                  port=int(os.environ.get("PORT", "26500"))) # Create grpc channel
worker = ZeebeWorker(grpc_channel=channel, poll_retry_delay=10, max_connection_retries=-1) # Create a zeebe worker
logging.info("Worker created!")

async def on_error(exception: Exception, job: Job):
    """
    on_error will be called when the task fails
    """
    logging.error(exception)
    await job.set_error_status(f"Failed to handle job {job}. Error: {str(exception)}")

@worker.task(task_type="utils-json-string-to-object", exception_handler=on_error) # Parse JSON
def utils_task(jsonString: str) -> dict:
    logging.info("Processing json string to object task")
    jsonObject = json.loads(jsonString.replace('\\n', '').replace('\\t', '').replace('\\r', '').replace('\\"', '"'))
    logging.info("Json string to object task processed")
    return {"response": jsonObject}

loop = asyncio.get_event_loop()
loop.run_until_complete(worker.work())