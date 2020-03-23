from django import forms


class ContactForm(forms.Form):

    user_name = forms.CharField(max_length=60, label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    user_email = forms.EmailField(label='', required=True)
    message = forms.CharField(label='', required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': '4'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "user_email":
                visible.field.widget.attrs['class'] = 'validate-required validate-email field-error'
                visible.field.widget.attrs['placeholder'] = 'Email Address'
            else:
                visible.field.widget.attrs['class'] = 'validate-required field-error'


    