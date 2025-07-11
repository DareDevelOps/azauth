import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv

# environment variables are locally maintained in a .env file
load_dotenv()


sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = ResourceManagementClient(credential = DefaultAzureCredential(), subscription_id=sub_id)

