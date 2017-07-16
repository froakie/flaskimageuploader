import uploader
import unittest
import os
import tempfile

class AppTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, uploader.app.config['DATABASE'] = tempfile.mkstemp()
		uploader.app.config['TESTING'] = True
		self.app = uploader.app.test_client()
		uploader.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(uploader.app.config['DATABASE'])


if __name__ == '__main__':
	unittest.main()