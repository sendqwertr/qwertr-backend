from django import forms
from django.contrib.auth import forms as auth_forms


class BootstrapStyleMixin(object):
    def __init__(self, *args, **kwargs):
        super(BootstrapStyleMixin, self).__init__(*args, **kwargs)
        for field in self.fields:
            widget_attrs = self.fields[field].widget.attrs.copy()
            widget_attrs.update({
                'class': widget_attrs.get('class', '') + ' form-control',
                'placeholder': self.fields[field].label,
            })
            self.fields[field].widget.attrs = widget_attrs


class AuthenticateForm(BootstrapStyleMixin, auth_forms.AuthenticationForm):
    pass
