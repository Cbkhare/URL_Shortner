##### in-memory DB access class #####

class DB(object):
    """
    This class is the in-memory db.
    It mimics a typical DB connector class.
    """
    def __init__(self):
        # DB schemas
        self.db = {}
        self.short_urls = {}

class URLShornterDBAcess(object):

    def __init__(self, db_object):
        self.db = db_object.db
        self.short_urls = db_object.short_urls 
        
    def insert(self, long_url, short_url):
        """
        This method inserts the details of the long URL and Short
        URL in the in-memory db.
        params:
            long_url: String
            short_url: String
        returns: None
        """
        if long_url in self.db:
            raise Exception("Shortened url exists")
        def _schema_db():
            return {
                "url": long_url,
                "short_url": short_url
            }
        def _schema_short_url():
            return {
                "long_url": long_url
            }
        self.db[long_url] = _schema_db()
        self.short_urls[short_url] = _schema_short_url()


    def get_short_url(self, long_url):
        """
        This method fetches the details of the short URL for the given
        long URL from the in-memory db.
        params:
            long_url: String
        returns: None/ Short_url String
        """
        if long_url not in self.db:
            return None 
        return self.db[long_url]["short_url"]
    
    def get_long_url(self, short_url):
        """
        This method fetches the details of the long URL for the given
        short URL from the in-memory db.
        params:
            short_url: String
        returns: None/ long_url String
        """
        if short_url not in self.short_urls:
            return None 
        return self.short_urls[short_url]["long_url"]

    def delete(self, long_url):
        """
        This method deletes the details of the long and the short
        URL for the given long_url URL from the in-memory db.
        params:
            long_url: String
        returns: String
        """
        if long_url not in self.db:
            return "Nothing to delete"
        else:
            short_url = self.db[long_url].get("short_url", "")
            del self.db[long_url]
            if short_url in self.short_urls:
                del self.short_urls[short_url]
            return "deleted"


