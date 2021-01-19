from hashlib import blake2b
from hmac import compare_digest

SECRET_KEY = b'U1FeX_omJWnVDFkTM9N6SLew0BqWp-xJgUTlMnzxxtQ='
AUTH_SIZE = 32

def sign(cookie : str) -> bytes:
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
    h.update(cookie.encode('utf-8'))
    return h.hexdigest().encode('utf-8')

def verify(cookie : str, sig : bytes) -> bool:
    return compare_digest(sign(cookie), sig)