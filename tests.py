from application import app

import unittest


class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.response = self.app.get("/", follow_redirects=True)

    def tearDown(self):
        pass

    def test_get_request(self):
        self.assertEqual(self.response.status_code, 200)

    def test_content_type(self):
        self.assertIn("text/html", self.response.content_type)

    def test_content(self):

        languages = ["Python", "JavaScript", "Ruby", "Java", "C"]

        for language in languages:
            self.assertIn(language, self.response.data.decode("utf-8"))

    def test_bootstrap_html(self):
        self.assertIn("bootstrap.min.css", self.response.data.decode("utf-8"))
        self.assertIn("bootstrap.min.js", self.response.data.decode("utf-8"))

    def test_jquery_html(self):
        self.assertIn("jquery-3.3.1.slim.min.js", self.response.data.decode("utf-8"))

    def test_popper_html(self):
        self.assertIn("popper.min.js", self.response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
