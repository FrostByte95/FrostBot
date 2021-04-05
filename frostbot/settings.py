"""Configuration settings for FrostBot"""
import os
import ssl

# Workaround for ssl error when using heroku
ssl_certs = ssl.create_default_context(cafile="")
ssl_certs.check_hostname = False
ssl_certs.verify_mode = ssl.CERT_NONE

DB_BACKEND = "db.postgresql.DBWrapper"
DB_CONNECTION = {
    "dsn": os.getenv("DATABASE_URL"),
    "max_size": 18,
    "ssl": ssl_certs
}
