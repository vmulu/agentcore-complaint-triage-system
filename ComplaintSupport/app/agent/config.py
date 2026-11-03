"""
dedicated space to load in the ENV file
"""

import os

AWS_REGION = os.getenv("AWS_REGION")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "")
BEDROCK_MAX_TOKENS = os.getenv("BEDROCK_MAX_TOKENS")