import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def get_env_variable(var_name, default_value=None):
    """Fetches an environment variable, returns default if not found."""
    return os.getenv(var_name, default_value)