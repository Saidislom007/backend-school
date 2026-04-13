from django.http import JsonResponse
from rest_framework import generics
from .models import *
from .serializers import *

# ============ HOME VIEW ============
def home(request):
    return JsonResponse({
        'message': '69-IDUM API ishlamoqda!',
        'status': 'success',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'api_blog': '/api/blog/',
            'api_teachers': '/api/teachers/',
            'api_gallery': '/api/gallery/photos/',
            'api_achievements': '/api/achievements/',
            'api_library': '/api/library/',
        }
    })

# ============ BLOG VIEWS ============
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# ============ TEACHER VIEWS ============
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# ============ GALLERY VIEWS ============
class GalleryPhotoListCreateView(generics.ListCreateAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

# ============ ACHIEVEMENT VIEWS ============
class AchievementListCreateView(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

# ============ LIBRARY VIEWS ============
class LibraryItemListCreateView(generics.ListCreateAPIView):
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        type_filter = self.request.query_params.get('type')
        if type_filter:
            queryset = queryset.filter(type=type_filter)
        return queryset