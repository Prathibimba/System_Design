import redis

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_cached_data(key):
    data = cache.get(key)
    if data:
        return data
    else:
        return None

def set_cached_data(key, value):
    cache.set(key, value)
