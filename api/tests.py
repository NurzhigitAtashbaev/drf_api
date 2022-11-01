from django.test import TestCase
from .models import Product
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIRequestFactory


class ProductTestCase(TestCase):
    def setUp(self):
        for i in range(1000):
            Product.objects.create(
                title='Hello, from testing !',
                price='6.8')

    def test_queryset_exists(self):
        queryset = Product.objects.all()
        self.assertTrue(queryset.exists())

    def test_queryset_count(self):
        queryset = Product.objects.all()
        self.assertEqual(queryset.count(), 1000)

    def test_check_id(self):
        product_object = Product.objects.first()
        object_with_id_1 = product_object.id
        self.assertEqual(object_with_id_1, 1)
        self.assertEqual(Product.objects.last().id, 1000)


class APITests(APITestCase):
    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """
        url = reverse('product-list')
        data = {
                "title": "Orange",
                "price": "150"
                }
        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Orange')
