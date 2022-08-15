from datetime import datetime
from django.http import HttpResponse
import json
from blog.models import Comment
from GlobalModels.Serializer import GetJson,SerializeModel


def CommentApi(request):
    try:
        Ojson = GetJson(request)
        Comments = Comment(User = Ojson["User"], Title = Ojson["Title"], Text = Ojson["Text"], Date = datetime.now())
        Comments.save()
        st = {
            "mensaje": "se ha guardado el mensaje"
        }
    except Exception as e:
        st = {
            "mensaje": "no se guardo el comentario"+ str(e)
        }    
    return HttpResponse(json.dumps(st),content_type="application/json")


def LeerComentario(request):
    try:
        comments = Comment.objects.all()

        comentario=[]
        for item in comments:
            comentario.append(SerializeModel(item))
        

        st = {
            "ComentariosExistentes": comentario
        }
    except Exception  as e:
        st = {
            "error": "no hay conexion"
        }
    return HttpResponse(json.dumps(st),content_type="aplication/json")


