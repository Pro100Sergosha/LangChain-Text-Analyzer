import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DB_NAME = os.getenv("DB_NAME", "database")

DB_URL = os.getenv("DB_URL", f"sqlite:///{DB_NAME}.db")
