from django import forms
from .models import Order, Category, Report
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Login",
        "autofocus": "",}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"}))


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class OrderCreateForm(BootstrapForm):
    image = forms.ImageField(label='Picture', required=False, widget=forms.FileInput(attrs = {"class":"form-contol",  "multiple":"", }))
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label=None)
    class Meta:
        model = Order
        fields = [
            'title',
            'count',
            'category',
            ]


class CategoryCreateForm(BootstrapForm):
    class Meta:
        model = Category
        fields = [
            'title',
            # 'slug',
            ]

class ReportCreateForm(BootstrapForm):
    class Meta:
        model = Report
        fields = [
            'date_month',
        ]



# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title','content','appoint_to','photo','typing']
#         # widgets = {
#         #     'title':forms.TextInput(attrs={"class":"form-control"}),
#         #     'content':forms.Textarea(attrs={"class":"form-control"}),
#         #     # 'appoint_to':forms.DateInput(attrs={"class":"form-control"}),
#         #     'appoint_to':forms.DateInput(attrs={"class":"form-control","id":"appoint_to","placeholder":"MM.DD.YYYY","type":"text"}),
#         #     'photo':forms.FileInput(attrs={"class":"form-control"}),
#         #     'typing':forms.Select(attrs={"class":"form-select"}),
#         # }


# class TypingForm(forms.ModelForm):
#     class Meta:
#         model = Typing
#         fields = '__all__'
#         # widgets = {
#         #     'title':forms.TextInput(attrs={"class":"form-control"}),
#         # }
