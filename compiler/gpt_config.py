import os
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env if present
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY not set. Create a .env file or set the environment variable.")

client = anthropic.Anthropic(api_key=api_key)