from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()

    class Meta:
        fields = "__all__"
