####### URL Shortner #######

import hashlib

from datetime import datetime

def generate_short_url(long_url):
    """
    This method generates a short URL string for the passed long URL.
    Long URL is appended with current date time to uniquely generate
    short URL for the given URL.
    encoding algorithm used for the string is MD5.
    """
    long_url += str(datetime.now())
    return hashlib.md5(long_url.encode('utf-8')).hexdigest()
    
