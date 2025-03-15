# from django.contrib.auth.models import User
# from rest_framework import serializers

# class RegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only = True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password2']
#         extra_kwargs = {
#             'password' :{
#                 'write_only' : True
#             }
#         }

#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError('Passwords are not same')
#         return data
    
#     def create(self, validated_data):
#         username = validated_data['username']
#         email = validated_data['email']
#         password = validated_data['password']
#         user = User.objects.create_user(username=username, email=email, password=password)
#         return user

from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSeril(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Parollar bir xil emas')
        return data
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        return user