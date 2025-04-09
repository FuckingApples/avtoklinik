import os

if os.getenv("PIPELINE") == "production":
    from .production import *
else:
    from .development import *
