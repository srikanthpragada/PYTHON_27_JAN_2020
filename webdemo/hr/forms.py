import django.forms as forms


class JobForm(forms.Form):
    id = forms.CharField(label="Job ID", max_length=10)
    title = forms.CharField(label="Job Title", max_length=50)
    minsal = forms.IntegerField(label="Min Salary")

