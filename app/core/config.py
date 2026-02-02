# Central configuration file
# Reads environment variables for app settings

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://username:password@localhost/dbname"
)
