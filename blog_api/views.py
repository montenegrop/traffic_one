from rest_framework import generics
from blog.models import Post
from .serializer import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class PostDefail(generics.RetrieveDestroyAPIViewj):
    pass