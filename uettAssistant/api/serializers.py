from rest_framework import serializers
from uettApp.models import *
from titlepage.models import *


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class SubjectSerializers(serializers.ModelSerializer):
    department = DepartmentSerializers(many=False)

    class Meta:
        model = Subject
        fields = "__all__"


class SemesterSerializers(serializers.ModelSerializer):
    department = DepartmentSerializers(many=False)
    subjects = SubjectSerializers(many=True)

    class Meta:
        model = Semester
        fields = "__all__"


class TitlePageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TitlePage
        fields = "__all__"
