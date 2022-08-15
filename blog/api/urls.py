from django.urls import path
from .views import CommentApi, LeerComentario

urlpatterns = [
    path('nuevo-Comentario/', CommentApi, name="CommentApi"),
    path('comentarios/', LeerComentario, name="LeerComentario"),
]