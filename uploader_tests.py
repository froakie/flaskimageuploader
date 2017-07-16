from flask import Flask, Request, request
from StringIO import StringIO
import unittest

RESULT = False

class TestFileUpload(unittest.TestCase):

    def test_1(self):

        class FileObj(StringIO):
            
            # Close file & remove from file system
            def tearDown(self):
                global RESULT
                RESULT = True
        
        class MyRequest(Request):

        	# Get file
            def _get_file_stream(*args, **kwargs):
                return FileObj()

        # Initialize app
        app = Flask(__name__)
        app.debug = True
        app.request_class = MyRequest

        @app.route("/", methods=['POST'])

        # Test file upload
        def upload():
            f = request.files['file']
            self.assertIsInstance(f.stream, FileObj,)
            f.tearDown()
            return 'OK'
            
        # Post image
        client = app.test_client()
        response = client.post('/', data = {'file': (StringIO('content'), 'test.jpg'),})
        self.assertEqual('OK', response.data,)
        global RESULT
        self.assertTrue(RESULT)

    def test_2(self):
        pass
        

if __name__ == '__main__':
	unittest.main()