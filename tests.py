from application import app

import json
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
        self.assertIn("jquery-3.3.1.slim.min.js",
                      self.response.data.decode("utf-8"))

    def test_popper_html(self):
        self.assertIn("popper.min.js", self.response.data.decode("utf-8"))


class TestDataRoute(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_request(self):
        response = self.app.get("/data", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_content_type(self):
        response = self.app.get("/data", follow_redirects=True)
        self.assertIn("application/json", response.content_type)

    def test_post_request(self):

        obj = json.dumps({"name": "automated-test", "language": "Python", "stargazers_count": 1, "forks_count": 1, "date": "Test Date",
                          "html_url": "automated-test-url", "description": "This is not a repo, it is an automated test result"})

        response = self.app.post(
            "/data", data=obj, headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_post_content_type(self):

        obj = json.dumps({"name": "automated-test", "language": "Python", "stargazers_count": 1, "forks_count": 1, "date": "Test Date",
                          "html_url": "automated-test-url", "description": "This is not a repo, it is an automated test result"})

        response = self.app.post(
            "/data", data=obj, headers={"Content-Type": "application/json"})
        self.assertIn("text/html", response.content_type)


if __name__ == "__main__":
    unittest.main()
