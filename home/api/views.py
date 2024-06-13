from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)
from .serializers import BlogSerializer
from ..models import Blog
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import BlogPagination


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ["id"]
    search_fields = ["title"]
    # pagination_class = BlogPagination
    
    # def get_queryset(self):
    #     queryset = Blog.objects.filter(draft=False)
    #     return queryset
    
# http://127.0.0.1:8000/blog-api/list/?search={value}


class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)


# http://127.0.0.1:8000/blog-api/update/{id}
