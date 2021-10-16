from rest_framework import serializers 
from .models import users
 
 
class userSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = users
        fields = ('id','first_name','last_name',
        'email_id','password','user_name')
