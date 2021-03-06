from django.db import models
from django.core import serializers
from django.apps import apps

class Serializer:
    def __init__(self, saved_dir=None, models=None):
        self.saved_dir = saved_dir if saved_dir else conf.BaseDir
        self.models = models if models else conf.models_to_dump

    def dump_models(self):
        for model in self.models:
            model_class = apps.get_model(model['name'])

            print "The Count of {} data that shoud be serialized:".format(model_class._meta.model_name), model_class.objects.count() 

            with open(r'./{}/{}_{}.json'.format(self.saved_dir, model_class._meta.app_label, model_class._meta.model_name), "w") as out:
                data = serializers.serialize('json', model_class.objects.all())
                out.write(data)


class DeSerializer:
    def __init__(self, read_dir=None, models=None):
        self.saved_dir = read_dir if read_dir else conf.BaseDir
        self.models = models if models else conf.models_to_dump

    def fields_included(self, model, excluded_fields=[]):
        fields = []
        for field in model._meta.fields:
            if field.name not in excluded_fields:
                fields.append(field)
        return fields

    def reload(self):
        for model in self.models:
            model_class = apps.get_model(model['name'])
            with open(r'./{}/{}_{}.json'.format(self.saved_dir, model_class._meta.app_label, model_class._meta.model_name), 'r') as myfile:
                data = myfile.read()

            for obj in serializers.deserialize("json", data):
                if not model_class.objects.filter(id=obj.object.pk):
                    print(obj.object)
                    fields = self.fields_included(model_class, model['excluded_fields'])
                    print(fields)
                    in_create_dic = {}
                    for field in fields:
                        in_create_dic.update({field.name: getattr(obj.object, field.name)})

                    model_class.objects.create(**in_create_dic)
                   
