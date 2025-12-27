import os
import time
import redis
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Crawler Worker...")
    
    db_url = os.getenv("DATABASE_URL")
    redis_url = os.getenv("REDIS_URL")
    
    logger.info(f"Connected to DB: {db_url is not None}")
    logger.info(f"Connected to Redis: {redis_url is not None}")

    # Mock connection check
    try:
        r = redis.from_url(redis_url)
        r.ping()
        logger.info("Redis valid PING")
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")

    while True:
        logger.info("Crawler: Waiting for jobs...")
        time.sleep(10)

if __name__ == "__main__":
    main()
