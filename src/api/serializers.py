from rest_framework import serializers
from sharing_code.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'lang', 'date')
