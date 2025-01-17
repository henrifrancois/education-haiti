from django import forms

from people.models import User
from people.models import UNIVERSITIES, Mentor, ToDo
# Create your forms here.

"""class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

        widgets = {
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'username',
                    'required' : True,
                }
            ),
            'password' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'required' : True,
                }
            )
        }"""


class MentorLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'undergrad_college')
        undergrad_college = forms.MultipleChoiceField(
            choices=UNIVERSITIES,
            label='Choose your university',
            initial='',
            widget=forms.SelectMultiple(),
            required=True
        )
        widgets = {
            'username' : forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'username',
                    'required': True,
                }
            ),
            'password': forms.PasswordInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'password',
                    'required': True,
                }
            )
        }


"""class RegisterForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ('email', 'username', 'password', 'rank')
        password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'email',
                    'required' : True,
                }
            ),
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'username',
                    'required' : True,
                }
            ),
            'password' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'required' : True,
                }
            ),
            'rank'     : forms.RadioSelect(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : "Mentor or mentee"
                },
            )
        }"""


class MentorUpdateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('grad_college','majors','interests','residency','phone','current_status','school_haiti','first_name',
                  'last_name','picture')
        picture = forms.ImageField(label='Upload your profile picture')
        widgets = {
            'grad_college': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Graduate College',
                    'required': True,
                }
            ),
            'majors': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your major(s), please separate each major with a comma',
                    'required': True,
                }
            ),
            'interests': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your interests, please separate each one with a comma',
                    'required': True,
                }
            ),
            'residency': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your state/city of residency',
                    'required': True,
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number',
                    'required': True,
                }
            ),
            'current_status': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your current status/work ... work work work work work',
                    'required': True,
                }
            ),
            'school_haiti': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'School in Haiti ... Institution Alea Touare',
                    'required': True,
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First Name',
                    'required': True,
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last Name',
                    'required': True,
                }
            ),
        }


class MentorRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'undergrad_college')
        password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
        undergrad_college = forms.MultipleChoiceField(
            choices=UNIVERSITIES,
            label='Choose your university',
            initial='',
            widget=forms.SelectMultiple(),
            required=True
                                    )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email',
                    'required': True,
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'username',
                    'required': True,
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'password',
                    'required': True,
                }
            )
        }


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('subject', 'expires',)
        widgets = {
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'What is this ToDo about',
                    'required': True,
                }
            ),
            'expires': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Should be enterd in the YYYY-MM-DD format. Ex: 2016-10-28',
                    'required': True,
                }
            ),
        }


class ToDoCompletionForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('completion',)
        completion = forms.CheckboxInput()


class MentorRegisterForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ('email', 'username', 'password', 'undergrad_college')
        password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
        undergrad_college = forms.MultipleChoiceField(
            choices=UNIVERSITIES,
            label = 'Choose your university',
            initial = '',
            widget = forms.SelectMultiple(),
            required = True
                                    )
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'email',
                    'required' : True,
                }
            ),
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'username',
                    'required' : True,
                }
            ),
            'password' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'required' : True,
                }
            )
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")

        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            exists = User.objects.get(email=email)
            raise forms.ValidationError("This email is already in use.")
        except User.DoesNotExist:
            return email
