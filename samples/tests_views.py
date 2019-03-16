from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import SampleStatus, SampleDetails, SampleResults


class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")

    def test_products_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
