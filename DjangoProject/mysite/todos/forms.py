# Application Specific
from todos.models import TodoTask

# Third Party
from django.forms import ModelForm, Textarea, CheckboxInput

__author__ = 'basit'


class AddTodoForm(ModelForm):

    class Meta:
        model = TodoTask
        fields = ('task_name', 'description', 'is_checked')
        widgets = {
            'description': Textarea,
            'is_checked': CheckboxInput
        }

