from rest_framework import serializers
from ads.models import Ad, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_avatar = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author_avatar(self, obj):
        request = self.context.get("request")
        if obj.author.avatar:
            return request.build_absolute_uri(obj.author.avatar.url)


class AdSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Ad"""
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'image', 'created_at')


class AdDetailSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для просмотра детальной информации по объявлению"""
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_email = serializers.CharField(source="author.email", read_only=True)
    author_phone = serializers.CharField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
