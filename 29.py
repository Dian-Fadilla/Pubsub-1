#
# Example pub/sub publish program
#
from google.cloud import pubsub_v1
from google.oauth2 import service_account
from datetime import datetime

#Project ID of Topic
PROJECT_ID = "hsc2020-04"
# Topic ID to publish to
TOPIC_ID = "NPM1704111010019"

# Credentials file
GOOGLE_APPLICATION_CREDENTIALS_PATH = r"D:\SEMESTER 7\PAK RAHMAD DAUD SEM7\KODE\NPM_1704111010019.json"

# Create credentials object
credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS_PATH)

# Create a publisher client to access pub/sub service
publisher = pubsub_v1.PublisherClient(credentials=credentials)

# Create topic object
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# Create message
message = "Data: " + str(datetime.now())
message = str.encode(message)
print("Nama: ", end="")
nama = input ()
nama = str.encode(nama)
print("NPM: ", end="")
npm = input ()
npm = str.encode(npm)

# Publish message
future = publisher.publish(topic_path, message)
future1 = publisher.publish(topic_path, nama)
future2 = publisher.publish(topic_path, npm)
print("future", future.result())