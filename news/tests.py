from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from news import factories as ff

from django.urls import reverse


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = ff.MyUserFactory()
        cls.post = ff.PostFactory(
            author_name=cls.user, title="test-title", link="https//:www.test.com"
        )

    def test_content(self):
        post = self.post
        expected_object_name = f"{post.title}" + f"{post.link}"
        self.assertEquals(expected_object_name, "test-titlehttps//:www.test.com")


class ViewPostTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = ff.MyUserFactory()
        cls.client = APIClient()

    def test_post_crud(self):
        data = {
            "author_name": self.user.id,
            "title": "test",
            "link": "https://www.test.com/",
        }
        self.client.force_authenticate(self.user)

        # create post
        response = self.client.post(reverse("api:post-list"), data, format="json")
        self.assertEquals(response.status_code, 201)

        # get posts
        response = self.client.get(reverse("api:post-list"), data, format="json")
        self.assertEquals(response.status_code, 200)

        # update post
        data.update({"title": "new test"})
        response = self.client.patch(
            reverse("api:post-detail", kwargs={"pk": self.user.id}), data, format="json"
        )

        self.assertEquals(response.status_code, 200)
        # delete post
        response = self.client.delete(
            reverse("api:post-detail", kwargs={"pk": self.user.id}), format="json"
        )
        self.assertEquals(response.status_code, 204)


class ViewCommentTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = ff.MyUserFactory()
        cls.client = APIClient()
        cls.post = ff.PostFactory(
            author_name=cls.user, title="test-title", link="https//:www.test.com"
        )

    def test_comment_crud(self):
        data = {
            "author_name": self.user.id,
            "post": self.post.id,
            "content": "test content",
        }
        self.client.force_authenticate(self.user)

        # create comment
        response = self.client.post(reverse("api:comment-list"), data, format="json")
        self.assertEquals(response.status_code, 201)

        # get comments
        response = self.client.get(reverse("api:comment-list"), data, format="json")
        self.assertEquals(response.status_code, 200)

        # update comment
        data.update({"content": "new content"})
        response = self.client.put(
            reverse("api:comment-detail", kwargs={"pk": 1}), data, format="json"
        )
        self.assertEquals(response.status_code, 200)

        # delete comment
        response = self.client.delete(
            reverse("api:comment-detail", kwargs={"pk": 1}), data, format="json"
        )
        self.assertEquals(response.status_code, 204)


class ViewUpvoteTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = ff.MyUserFactory()
        cls.client = APIClient()
        cls.post = ff.PostFactory(
            author_name=cls.user, title="test-title", link="https//:www.test.com"
        )

    def test_comment_crud(self):
        data = {
            "author": self.user.id,
            "post": self.post.id,
        }
        self.client.force_authenticate(self.user)

        # create upvote
        response = self.client.post(reverse("api:upvote-list"), data, format="json")
        self.assertEquals(response.status_code, 201)

        # get upvotes
        response = self.client.get(reverse("api:upvote-list"), data, format="json")
        self.assertEquals(response.status_code, 200)

        # delete upvote
        response = self.client.delete(
            reverse("api:upvote-detail", kwargs={"pk": 1}), data, format="json"
        )
        self.assertEquals(response.status_code, 204)
