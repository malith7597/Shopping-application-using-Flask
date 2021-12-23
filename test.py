from flask.typing import StatusCode
from werkzeug.wrappers import response
import os

import unittest



try:
    from run import app
    import unittest
except Exception as e:
    print("Some Modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):
    #check for the response 200
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get('/home')
        StatusCode=response.status_code
        self.assertEqual(StatusCode,200)

    #check query a product using valid id

    def test_index_query_product_invalid_id(self):
        tester=app.test_client(self)
        response=tester.get('/search/1')
        StatusCode=response.status_code
        self.assertEqual(StatusCode,200)

    #check query a product using invalid id
    def test_index_query_product_using_invalid_id(self):
        tester=app.test_client(self)
        response=tester.get('/search/50')
        StatusCode=response.status_code
        self.assertEqual(StatusCode,404)

    def test_index_update(self):
        tester=app.test_client(self)
        response=tester.post('/update',data=dict(id='1',new_quantity='1'), follow_redirects=True)
        self.assertIn(b'Message: Successfully updated!.',response.data)
    #update on unknown product value.
    def test_index_update_invalid(self):
        tester=app.test_client(self)
        response=tester.post('/update',data=dict(id='15',new_quantity='15'), follow_redirects=True)
        self.assertIn(b'Message: Product is not available to update',response.data)

    def test_index_buy_invalid(self):
        tester=app.test_client(self)
        response=tester.post('/buy',data=dict(id='1',card_number='1234123412341234',cvv='123',expiry_date='12/03/2024',quantity='2'), follow_redirects=True)
        self.assertIn(b'Message: Error!.Stocks are not available',response.data) 
    
    def test_index_simulatenous(self):
        tester=app.test_client(self)
        response=tester.post('/buy',data=dict(id='6',card_number='1234123412341234',cvv='123',expiry_date='12/03/2024',quantity='8'), follow_redirects=True)
        self.assertIn(b'Message: Item Purchased!.Deducted 640 from your account.',response.data)
        response1= tester.post('/buy',data=dict(id='6',card_number='1234123412341234',cvv='123',expiry_date='12/03/2024',quantity='6'), follow_redirects=True)
        self.assertIn(b'Message: Error!.Stocks are not available',response1.data) 
    def test_index_buy_valid(self):
        tester=app.test_client(self)
        response=tester.post('/buy',data=dict(id='2',card_number='1234123412341234',cvv='123',expiry_date='12/03/2024',quantity='1'), follow_redirects=True)
        self.assertIn(b'Message: Item Purchased!.Deducted 850 from your account.',response.data)

if __name__=="__main__":
    unittest.main()