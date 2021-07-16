from google.oauth2 import service_account
from google.cloud import datastore
from datetime import datetime

#Project ID where Datastore is located
PROJECT_ID = "hsc2020-04"

# Credentials file
GOOGLE_APPLICATION_CREDENTIALS_PATH = r"D:\SEMESTER 7\PAK RAHMAD DAUD SEM7\KODE\NPM_1704111010019.json"
# Create credentials object
credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS_PATH)


def simpan(nama, npm):
    # Create a client to access the datastore
    client = datastore.Client(project=PROJECT_ID, credentials=credentials)

    # Create a new key to store a new entity
    newKey = client.key("NPM")

    # Create a new entity
    newEntity = datastore.Entity(newKey)
    
    # Fill in its data
    newEntity.update({
        "created": datetime.now(),
        "nama": nama(input),
        "npm": npm(input),
    })

    # Store it
    client.put(newEntity)

simpan(input, input)