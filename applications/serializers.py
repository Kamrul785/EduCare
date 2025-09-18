from rest_framework import serializers
from .models import Application, Enrollment, Topic, Assignment, Review

class ApplicationSerializer(serializers.ModelSerializer):
    applicant_email = serializers.ReadOnlyField(source="applicant.email")
    tuition_title = serializers.ReadOnlyField(source="tuition.title")

    class Meta:
        model = Application
        fields = ["id", "tuition", "tuition_title", "applicant_email", "status", "applied_at"]
        read_only_fields = ["id", "tuition_title", "applicant_email", "status", "applied_at"]


class EnrollmentSerializer(serializers.ModelSerializer):
    student_email = serializers.ReadOnlyField(source="student.email")
    tuition_title = serializers.ReadOnlyField(source="tuition.title")

    class Meta:
        model = Enrollment
        fields = ["id", "tuition", "tuition_title", "student_email", "enrolled_at"]
        read_only_fields = ["id", "tuition_title", "student_email", "enrolled_at"]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'enrollment', 'title', 'description', 'completed']
        read_only_fields = ['id', 'enrollment']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'enrollment', 'title', 'description', 'due_date']
        read_only_fields = ['id', 'enrollment']
        

class ReviewSerializer(serializers.ModelSerializer):
    student_email = serializers.ReadOnlyField(source="student.email")
    tuition_title = serializers.ReadOnlyField(source="tuition.title")

    class Meta:
        model = Review
        fields = ["id", "tuition", "tuition_title", "student_email", "rating", "comment", "created_at"]
        read_only_fields = ["id", "student_email", "tuition_title", "created_at"]
