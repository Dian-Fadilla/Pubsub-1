#
# Example pub/sub subscribe pull version program
#
from google.cloud import pubsub_v1
from google.oauth2 import service_account
from concurrent.futures import TimeoutError

#Project ID of Topic
PROJECT_ID = "hsc2020-04"
# Subscription ID to subscribe to
SUBSCRIPTION_ID = "NPM1704111010019"

# Credentials file
GOOGLE_APPLICATION_CREDENTIALS_PATH = r"D:\SEMESTER 7\PAK RAHMAD DAUD SEM7\KODE\NPM_1704111010019.json"
# Create credentials object*
credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS_PATH)

# Callback function, called when a message arrives
def callback(message):
    # Do somwething with the message
    print(f"Message received:")
    print(f"{message}.")

    # Need to acknowledge receipt, if not will be resent
    message.ack()
def callback(nama):
    # Do somwething with the message
    print(nama)
    nama.ack()
def callback(npm):
    # Do somwething with the message
    print(npm)
    # Need to acknowledge receipt, if not will be resent
    npm.ack()

# Crete a subscriber client to access pub/sub service
subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

# Create subscription object
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

# Subscribe (start receiving message) and give it the callback function name that will process incoming message
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
streaming_pull_future1 = subscriber.subscribe(subscription_path, callback=callback)
streaming_pull_future2 = subscriber.subscribe(subscription_path, callback=callback)

try:
    streaming_pull_future.result(timeout=5) 
    streaming_pull_future1.result(timeout=5)
    streaming_pull_future2.result(timeout=5)

except TimeoutError as err:
    streaming_pull_future.cancel()
    print(f"Exception: {err}.")
    streaming_pull_future1.cancel()
    print(f"Exception: {err}.")
    streaming_pull_future2.cancel()
    print(f"Exception: {err}.")

# End subscription (stop receiving message)
subscriber.close()