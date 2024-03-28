from rest_framework import serializers
from .models import githubRepo

class repoSerializer(serializers.ModelSerializer):
        class Meta:
                    model = githubRepo
                    fields  =   ('id', 'name', 'description', 'type')