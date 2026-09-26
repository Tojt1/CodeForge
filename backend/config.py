from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

jwt_secret = os.getenv("JWT_SECRET")
jwt_algorithm = os.getenv("JWT_ALGORITHM")

REPOSITORY_PATH = Path("/data/repositories")