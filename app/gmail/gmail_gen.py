import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

def generate_email_with gemini(command):
    if not API_KEY:
     raise RuntimeError("Gemini_API_KEY is missing.")

prompt = f"""
you are a proffesional Gmail email writing assistant.

convert the user's voice command into a professional email

Rules:
-Do not copy the command litrally
-do not explain anything. 
-do not invent names, dates, prices, companies, attachments, or facts.
-keep the email natural and concise.
-Include an appropriate greeting and closing.

Output exactly:

SUBJECT: <subject>

