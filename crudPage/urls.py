from django.urls import path
from .views import *

app_name = 'pagecrud'
urlpatterns = [
    path('index/', index, name='index'),
    path('catalog/', CatalogView.as_view(), name='catalogcrud'),
    path('catalogDelete/<int:delete_id>/', catalogDelete, name='catalogdelete'),
    path('catalogUpdate/<int:id_catalog>/', catalogUpdate, name='catalogupdate'),
    path('repository/', RepositoryView.as_view(), name='repositorycrud'),
    path('repositoryDelete/<int:delete_id>/', repositoryDelete, name='repositorydelete'),
    path('repositoryUpdate/<int:id_repository>/', repositoryUpdate, name='repositoryupdate'),
    path('journalDelete/<int:delete_id>/', journalDelete, name='journaldelete'),
    path('journalUpdate/<int:id_journal>/', journalUpdate, name='journalupdate'),
    path('journal/', JournalView.as_view(), name='journalcrud'),
]