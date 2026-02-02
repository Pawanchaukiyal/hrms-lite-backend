# Central configuration file
# Stores environment-based settings like database URL

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)