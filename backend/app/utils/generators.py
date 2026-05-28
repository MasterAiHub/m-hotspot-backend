import random
import string

def generate_voucher_code(length: int = 8) -> str:
    """Generate a random alphanumeric voucher code."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
