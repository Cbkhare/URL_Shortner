##### in-memory DB access class #####

class DB(object):
    def __init__(self):
        self.db = {}

class URLShornterDBAcess(object):

    def __init__(self, db_object):
        self.db = db_object.db
        
    def insert(self, long_url, short_url):
        if long_url in self.db:
            raise Exception("Shortened url exists")
        def _schema():
            return {
                "url": long_url,
                "short_url": short_url # to be generated 
            }
        self.db[long_url] = _schema()

    def get(self, long_url):
        if long_url not in self.db:
            return None 
        return self.db[long_url]

    def delete(self, long_url):
        if long_url not in self.db:
            return "Nothing to delete"
        else:
            del self.db[long_url]
            return "deleted"


