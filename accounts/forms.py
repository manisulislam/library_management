
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import UserAccount

GENDER_TYPE=(
    ('Male','Male'),
    ('Female','Female'),
    
)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required',}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'id':'required',}))
    phone_no=forms.IntegerField()
    gender_type=forms.ChoiceField(choices=GENDER_TYPE)
    
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','birth_date','address','phone_no','gender_type']
    
    
        
    def save(self, commit=True):
        our_user=super().save(commit=False)
        if commit == True:
            our_user.save()
            birth_date=self.cleaned_data['birth_date']
            address=self.cleaned_data['address']
            phone_no=self.cleaned_data['phone_no']
            gender_type=self.cleaned_data['gender_type']
            
            UserAccount.objects.create(
                user=our_user,
                account_no=10000+our_user.id,
                birth_date=birth_date,
                address=address,
                phone_no=phone_no,
                gender_type=gender_type)
        return our_user