from django.forms import ModelForm
from add_code.models import Code

class CodeForm(ModelForm):
    class Meta:
        model = Code
        fields = ['Title', 'Content', 'Date', 'Language']
