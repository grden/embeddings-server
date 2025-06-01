from dotenv import load_dotenv
load_dotenv()
import os

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
# SIMILARITY_THRESHOLD: float = 0.75  # Adjust as needed 