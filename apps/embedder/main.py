import os
import time
import redis
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Embedder Worker...")
    
    db_url = os.getenv("DATABASE_URL")
    redis_url = os.getenv("REDIS_URL")
    
    while True:
        logger.info("Embedder: Waiting for jobs...")
        time.sleep(10)

if __name__ == "__main__":
    main()
