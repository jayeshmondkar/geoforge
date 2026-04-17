from fastapi import Header, HTTPException

# API keys (later move to DB)
API_KEYS = {
    "test-key-123": "user"
}

# Usage tracking (in-memory)
USAGE = {}

# Rate limit per key
MAX_REQUESTS = 10


def verify_api_key(x_api_key: str = Header(...)):
    # 🔐 Validate API key
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # 📊 Get usage count
    count = USAGE.get(x_api_key, 0)

    # 🚫 Rate limit check
    if count >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # ✅ Increment usage
    USAGE[x_api_key] = count + 1

    return API_KEYS[x_api_key]