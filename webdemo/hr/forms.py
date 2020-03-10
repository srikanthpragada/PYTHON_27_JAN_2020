import django.forms as forms
from .models import Book


class JobForm(forms.Form):
    id = forms.CharField(label="Job ID", max_length=10)
    title = forms.CharField(label="Job Title", max_length=50)
    minsal = forms.IntegerField(label="Min Salary")



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'