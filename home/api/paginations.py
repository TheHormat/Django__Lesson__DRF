from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination):
    page_size = 2