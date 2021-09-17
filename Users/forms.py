from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User,Treatment,Doctor,Patient,Symptom, QnA
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from crispy_forms.helper import FormHelper

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model =  Treatment
        fields = ["Appointment"]
        widgets = {
            'Appointment': DateInput(),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model =  QnA
        fields = ["Question"]

class AnswerForm(forms.ModelForm):
    class Meta:
        model =  QnA
        fields = ["Answer"]

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['email',]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email']

class LoginUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password']
    
    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_errors = False
        

class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(),validators=[validate_password]) #uncomment when using password validation
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password1','password2']

class Forgot_email_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class Forgot_Password_Form(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(),validators=[validate_password]) # to use django validation
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['password1','password2']


class Register_Doc(forms.ModelForm):
    class Meta:
        model=Doctor
        exclude = ['user']
        widgets = {
            'lat' : forms.HiddenInput(),
            'lon' : forms.HiddenInput()
        }


class Register_Patient(forms.ModelForm):
    class Meta:
        model=Patient
        exclude = ['user']

class Prescription(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['Prescription']

class Symptoms(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['SymptomList', 'lat', 'lon']
        widgets = {
            'lat' : forms.HiddenInput(),
            'lon' : forms.HiddenInput()
        }
    
    def __init__ (self, *args, **kwargs):
        super(Symptoms, self).__init__(*args, **kwargs)
        self.fields["SymptomList"].widget = forms.widgets.CheckboxSelectMultiple()
        l = Symptom.objects.all()
        choices = []
        for ob in l:
            choices.append((ob.id,ob.Name))
        choices.sort(key=self.func)
        self.fields["SymptomList"].choices = choices

    
    def func(self,a):
        return a[1]
