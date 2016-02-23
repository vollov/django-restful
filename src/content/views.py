from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all().order_by('-created_at')
    serializer_class = PageSerializer
