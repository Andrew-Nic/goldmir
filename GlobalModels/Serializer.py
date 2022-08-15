import json
from django.forms.models import model_to_dict

def GetJson(request): 
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' 
    print(is_ajax)
    if is_ajax and request.method == "POST": 
        json_str = request.body.decode(encoding='UTF-8') 
        json_obj = json.loads(json_str) 
    return json_obj 


def serialize(obj):
    dictionary = obj.__dict__ 
    return json.loads(json.dumps(dictionary,default=str))

def SerializeModel(obj):
		InvalidFields = ["Password","PIN"]
		return json.loads(json.dumps(model_to_dict(obj, 
		fields=[field.name for field in obj._meta.fields if (field.name not in InvalidFields)]), indent=4, sort_keys=True, default=str))