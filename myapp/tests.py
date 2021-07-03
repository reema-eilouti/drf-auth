from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username = 'tester', password = 'pass')
        test_user.save()

        test_post = Post.objects.create(
            title = 'test0',
            author = test_user,
            body = 'test1'
        )
        test_post.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.title, 'test0')
        self.assertEqual(post.body, 'test1')