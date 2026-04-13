from django.urls import path
from . import views

urlpatterns = [
    # Blog
    path('blog/', views.BlogPostListCreateView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog-detail'),
    
    # Teachers
    path('teachers/', views.TeacherListCreateView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    
    # Gallery
    path('gallery/photos/', views.GalleryPhotoListCreateView.as_view(), name='gallery-photos'),
    
    # Achievements
    path('achievements/', views.AchievementListCreateView.as_view(), name='achievement-list'),
    
    # Library
    path('library/', views.LibraryItemListCreateView.as_view(), name='library-list'),
]