# tests/test_db.py

import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Drop tables and close connection
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content='Hello world, I\'m John!'
        )
        self.assertEqual(first_post.id, 1)

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world, I\'m Jane!'
        )
        self.assertEqual(second_post.id, 2)

        # ✅ TODO: Get timeline posts and assert they are correct
        posts = list(TimelinePost.select().order_by(TimelinePost.created_at.desc()))
        self.assertEqual(len(posts), 2)

        self.assertEqual(posts[0].name, 'Jane Doe')
        self.assertEqual(posts[0].email, 'jane@example.com')
        self.assertEqual(posts[0].content, 'Hello world, I\'m Jane!')

        self.assertEqual(posts[1].name, 'John Doe')
        self.assertEqual(posts[1].email, 'john@example.com')
        self.assertEqual(posts[1].content, 'Hello world, I\'m John!')
