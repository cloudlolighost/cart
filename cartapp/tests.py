from django.test import TestCase
# from cartapp.models import OrdersModel
# Create your tests here.


class CartTests(TestCase):
    def test_error_mail01(self):
        user = {'CustomerName':'jeff', 'CustomerEmail': '123','CustomerAddress': 'FCU', 'CustomerPhone': '0231513254'}
        r = self.client.post('/cartok/', user)         
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/cartorder/')

    def test_error_mail02(self):
        user = {'CustomerName':'jeff', 'CustomerEmail': 'sdfsdfsdfsdf','CustomerAddress': 'FCU', 'CustomerPhone': '0231513254'}
        r = self.client.post('/cartok/', user)         
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/cartorder/')
        
    def test_error_mail03(self):
        user = {'CustomerName':'jeff', 'CustomerEmail': 'dfsdf@2f56.156.254','CustomerAddress': 'FCU', 'CustomerPhone': '0231513254'}
        r = self.client.post('/cartok/', user)         
        self.assertEqual(r.status_code, 200)
        
    def test_error_mail04(self):
        user = {'CustomerName':'jeff', 'CustomerEmail': 'dfsdf2f56.156.254','CustomerAddress': 'FCU', 'CustomerPhone': '02315132'}
        r = self.client.post('/cartok/', user)         
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/cartorder/')

    def test_error_mail05(self):
        user = {'CustomerName':'jeff', 'CustomerEmail': 'dasd@dad.com','CustomerAddress': 'FCU', 'CustomerPhone': '0231513254'}
        r = self.client.post('/cartok/', user)         
        self.assertEqual(r.status_code, 200)
        
