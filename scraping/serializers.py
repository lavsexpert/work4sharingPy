from rest_framework.serializers import ModelSerializer

from scraping.models import Employee, Request, Skill
from random import randint


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name','isset','link',)

class RequestSerializer(ModelSerializer):

    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Request
        fields = ('id', 'position', 'status', 'skills_text', 'skills')
        extra_kwargs = {'skills_text': {'write_only': True}}


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'position', 'status', 'vacancy', 'conformity', 'skills')

def mockup_employee_serializer(employee_view, *args, **kwargs):
    '''
    Мокап для вывода данных.
    Когда будут связи между моделями - лучше использовать ModelSerializer
    '''

    my_obj = type('MyObject', (), {})
    d = my_obj()
    d.data = list()

    for item in args[0]:
        if item.skills:
            skills = item.skills.splitlines()
        else: 
            skills = []

        d.data.append({
            'id': item.id,
            'position': item.position,
            'status': item.status,
            'vacancy': '',
            'conformity': randint(2, 10) * 10,
            'skills': [{'name': skill, 'isset': True, 'link': 'https://google.com'} for skill in skills],
        }) 

    return d

