from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('url', 'title', 'created_at')
