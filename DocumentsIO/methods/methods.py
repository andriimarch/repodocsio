import requests
from faker import Faker
fake = Faker()

def getRequestDocumentsIo():
    mainPageRequest = requests.get("https://www.documents.io/waiting-list")
    return mainPageRequest.json()