import unittest
from main import app

class CurrencyConverterTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_valid_conversion(self):
        response = self.app.get('/convert?source=USD&target=JPY&amount=$1,525')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['msg'], 'success')
        self.assertEqual(data['amount'], '$170,496.53')

    def test_invalid_currency(self):
        response = self.app.get('/convert?source=EUR&target=JPY&amount=$1,000')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'Invalid source or target currency')

    def test_invalid_amount(self):
        response = self.app.get('/convert?source=USD&target=JPY&amount=invalid')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'Invalid amount')

if __name__ == '__main__':
    unittest.main()
