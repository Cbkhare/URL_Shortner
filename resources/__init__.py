##### in-memory DB access class #####


class DB(object):

    def __init__(self):
        self.db = {}

class DbOperate(object):

    def __init__(self, db_object):
        self.db = db_object.db
