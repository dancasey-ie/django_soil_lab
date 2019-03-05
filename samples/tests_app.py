from django.apps import apps
from django.test import TestCase
from .apps import SampleConfig


class TestSampleConfig(TestCase):

    def test_app(self):
        self.assertEqual("sample", SampleConfig.name)
        self.assertEqual("samples", apps.get_app_config("samples").name)