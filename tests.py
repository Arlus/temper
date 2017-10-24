import temper
import unittest
import io
import csv
from temper import format_data


class AppTestCase(unittest.TestCase):
    def setUp(self):
        temper.app.testing = True
        temper.app.config['DEBUG'] = True
        self.app = temper.app.test_client()
        self.assertEqual(temper.app.debug, True)

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def data_import(self):
        output = io.BytesIO()
        writer = csv.writer(output)
        writer.writerow("3121,2016-07-19,40,0,0")
        writer.writerow("3122,2016-07-19,40,0,0")
        data = format_data(output.getvalue())
        self.assertEqual(data, [100, 100, 100, 0, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
