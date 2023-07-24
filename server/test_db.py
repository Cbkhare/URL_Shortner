import unittest
from db import URLShornterDBAcess, DB

class TestDBMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.db_conn = URLShornterDBAcess(DB())
        self.db_conn.insert(long_url="dummy_long_url",
                            short_url="dummy_short_url"
                            )
        return super().setUp()

    def test_get_short_url(self):
        short_url = self.db_conn.get_short_url("dummy_long_url")
        self.assertEqual("dummy_short_url", short_url)

    def test_get_long_url(self):
        long_url = self.db_conn.get_long_url("dummy_short_url")
        self.assertEqual("dummy_long_url", long_url)

    def test_get_short_url_negative(self):
        short_url = self.db_conn.get_short_url("dummy_url")
        self.assertEqual(None, short_url)

    def test_get_long_url_negative(self):
        long_url = self.db_conn.get_long_url("dummy_url")
        self.assertEqual(None, long_url)
    
    def tearDown(self) -> None:
        self.db_conn.delete("dummy_long_url")
        return super().tearDown()
    

if __name__ == '__main__':
    unittest.main()