from django.db import models
from django.db import models
from django.conf import settings
from tuition.models import Tuition
# Create your models here.

class Application(models.Model):
    STATUS_PENDING = "PENDING"
    STATUS_ACCEPTED = "ACCEPTED"
    STATUS_REJECTED = "REJECTED"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
    ]

    tuition = models.ForeignKey(
        Tuition, 
        on_delete=models.CASCADE, 
        related_name="applications"
    )
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="applications"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("tuition", "applicant")  

    def __str__(self):
        return f"{self.applicant.email} : {self.tuition.title} ({self.status})"


class Enrollment(models.Model):
    
    tuition = models.ForeignKey(
        Tuition, 
        on_delete=models.CASCADE, 
        related_name="enrollments"
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="enrollments"
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("tuition", "student")
    
    def __str__(self):
        return f"{self.student.email} enrolled in {self.tuition.title}"


class Topic(models.Model):
    enrollment = models.ForeignKey(
        Enrollment, 
        on_delete=models.CASCADE, 
        related_name="topics"
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'Completed' if self.completed else 'Pending'})"


class Assignment(models.Model):
    enrollment = models.ForeignKey(
        Enrollment, 
        on_delete=models.CASCADE,
        related_name="assignments"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    tuition = models.ForeignKey(
        Tuition,
        on_delete=models.CASCADE,
        related_name = 'reviews'
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="reviews"
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("tuition", "student") 

    def __str__(self):
        return f"{self.student.email}: {self.tuition.title} ({self.rating};{self.comment})"