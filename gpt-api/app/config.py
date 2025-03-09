import os
import uuid

base = {
    'DEBUG': False,
    'SECRET_KEY': uuid.uuid4().hex,
    "DB": os.getenv("DB")
}