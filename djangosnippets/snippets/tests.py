from django.test import TestCase
from django.http import HttpRequest
from snippets.views import top

# Create your tests here.


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(200, response.status_code)


    def test_top_returns_expected_content(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(b"Hello World", response.content)
