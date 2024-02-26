from rest_framework import serializers
from django.contrib.auth.models import User
from medical.models import medicalmedicines
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages





                              

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicalmedicines
        fields = "__all__"                                             