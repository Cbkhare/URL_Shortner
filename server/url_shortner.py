####### URL Shortner #######

import hashlib


def generate_short_url(long_url):
    return hashlib.md5(long_url.encode('utf-8')).hexdigest()
    
