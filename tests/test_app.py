# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        assert "<title>Learning Something</title>" in html

    def test_timeline(self):
      from app import TimelinePost
      TimelinePost.delete().execute()

      response = self.client.get("/api/timeline_post")
      self.assertEqual(response.status_code, 200)
      self.assertTrue(response.is_json)
      data = response.get_json()
      self.assertIn("timeline_posts", data)
      self.assertEqual(len(data["timeline_posts"]), 0)

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        assert "<h1>My Thoughts Timeline" in html or "Timeline" in html

    def test_post_timeline(self):
        response = self.client.post("/api/timeline_post", data={
            "name": "Test User",
            "email": "test@example.com",
            "content": "Testing post"
        })
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        assert json_data["name"] == "Test User"
        assert json_data["email"] == "test@example.com"
        assert json_data["content"] == "Testing post"

    def test_post_timeline(self):
      response = self.client.post("/api/timeline_post", data={
          "name": "Test User",
          "email": "test@example.com",
          "content": "This is a test post"
      })
      self.assertEqual(response.status_code, 200)
      json_data = response.get_json()
      self.assertEqual(json_data["name"], "Test User")
      self.assertEqual(json_data["email"], "test@example.com")
      self.assertEqual(json_data["content"], "This is a test post")

    def test_timeline_page(self):
      response = self.client.get("/timeline")
      self.assertEqual(response.status_code, 200)
      html = response.get_data(as_text=True)
      self.assertIn("<title>Timeline</title>", html)


    def test_malformed_timeline_post(self):
        # Missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(response.status_code, 400)

        # Empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        self.assertEqual(response.status_code, 400)

        # Invalid email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world!"
        })
        self.assertEqual(response.status_code, 400)
