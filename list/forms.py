from django.forms import ModelForm
from list.models import List

class ListCreateForm(ModelForm):
    class Meta:
        model = List
        fields = [
            'name', 
            'done',
        ]