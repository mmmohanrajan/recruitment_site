from django.urls import path, include

from api.v1.views import (	ApplicationAPIView,
							ApplicationDetailAPIView, 
							ApplicationAcceptAPIView,
							OpeningsAPIView, 
							OpeningsDetailAPIView,)

app_name = 'api'

urlpatterns = [
    path('applications', ApplicationAPIView.as_view(), name='app-creat'),
    path('applications/<int:pk>', ApplicationDetailAPIView.as_view(), name='app-detail'),
    path('applications/<int:pk>/accept', ApplicationAcceptAPIView.as_view(), name='app-accept'),
    path('openings', OpeningsAPIView.as_view(), name='openings-create'),
    path('openings/<int:pk>', OpeningsDetailAPIView.as_view(), name='openings-detail'),
]