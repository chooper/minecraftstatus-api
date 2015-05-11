import app
import unittest

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_root_404s(self):
        rv = self.app.get('/')
        assert '404 NOT FOUND' == rv.status

    def test_playersonline_noserver_404s(self):
        rv = self.app.get('/playersonline/')
        assert '404 NOT FOUND' == rv.status

    # TODO(charles) test mocked responses

if __name__ == '__main__':
    unittest.main()

