from django import forms
from django.core import validators

### check_for_z fun used as a custom validators ###
### Example: name = forms.CharField(validators=[check_for_z])
###################################################
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name needs to start with "z"')
###################################################

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify email')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails don't match")

    #bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    ### clean_ method used to check bot_catcher ###
    ###############################################
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("Caught a bot sleeping")
    ###################################################
