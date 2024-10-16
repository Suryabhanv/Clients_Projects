from django.urls import path
from .views import ProjectListCreateView
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView, ProjectCreateView, UserAssignedProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('api/clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),  # Use <int:pk> here
    path('clients/<int:pk>/projects/', ProjectCreateView.as_view(), name='client-projects'),
    path('projects/', UserAssignedProjectsView.as_view(), name='user-projects'),

]


