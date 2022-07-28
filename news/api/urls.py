from django.urls import include, path
from news.api.views import PostViewSet, CommentViewSet, UpvoteViewSet

app_name = "api"


post_list = PostViewSet.as_view({"get": "list", "post": "create"})
post_detail = PostViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
comment_list = CommentViewSet.as_view({"get": "list", "post": "create"})
comment_detail = CommentViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
upvote_list = UpvoteViewSet.as_view({"get": "list", "post": "create"})
upvote_detail = UpvoteViewSet.as_view({"delete": "destroy"})

urlpatterns = [
    path("posts/", post_list, name="post-list"),
    path("post/<int:pk>/", post_detail, name="post-detail"),
    path("comments/", comment_list, name="comment-list"),
    path("comment/<int:pk>/", comment_detail, name="comment-detail"),
    path("upvotes/", upvote_list, name="upvote-list"),
    path("upvote/<int:pk>/", upvote_detail, name="upvote-detail"),
]
