from django.urls import path,include
from rest_framework_nested import routers
from tuition.views import TuitionViewSet
from applications.views import ApplicationViewSet, EnrollmentViewSet, TopicViewSet, AssignmentViewSet,ReviewViewSet

router = routers.DefaultRouter()
router.register('tuitions',TuitionViewSet, basename='tuitions')
router.register("applications", ApplicationViewSet, basename="applications")
router.register("enrollments", EnrollmentViewSet, basename="enrollments")

enrollment_router = routers.NestedDefaultRouter(router, "enrollments", lookup="enrollment")
enrollment_router.register('topics', TopicViewSet, basename='enrollment-topics')
enrollment_router.register('assignments', AssignmentViewSet, basename='enrollment-assignments')

router.register('reviews',ReviewViewSet,basename='reviews')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(enrollment_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
