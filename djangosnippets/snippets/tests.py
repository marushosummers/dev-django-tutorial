from django.test import TestCase
from django.http import HttpRequest
from snippets.views import top


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(200, response.status_code)


    def test_top_returns_expected_content(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(b"Hello, world!", response.content)

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(b"Hello, world!", response.content)
