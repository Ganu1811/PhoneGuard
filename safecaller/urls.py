from django.urls import path
from safecaller import views

urlpatterns = [
    path('user/', views.UserProfileListView.as_view(), name = 'user'),
    path('user/create/', views.UserProfileCreateView.as_view(), name='user-create'),
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),
    path('spamreport/create/', views.SpamReportCreateView.as_view(), name = 'spamreport-create'),
    path('spamreport/', views.SpamReportListView.as_view(), name = 'spamreportlist')
]