import os
from dotenv import load_dotenv

load_dotenv()


DESTINATION_URL = os.getenv("URL", default="https://jservice.io/api/random?count=1")
