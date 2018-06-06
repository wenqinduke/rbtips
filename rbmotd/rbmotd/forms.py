import hashlib

from django import forms
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_bytes

from djblets.extensions.forms import SettingsForm
from list_edit_widget_with_clear_button import ListEditWidgetWithClearButton

class MotdSettingsForm(SettingsForm):
    enabled = forms.BooleanField(initial=False, required=False)
    message = forms.CharField(
        max_length=512,
        required=False,
        help_text=_('This field expects valid HTML. Entities must be '
                    'properly escaped.'),
        widget=forms.TextInput(attrs={
            'size': 100,
        }))
    enabled_tips = forms.BooleanField(initial=False, required=False)
    tips = forms.CharField(
        required=False,
        help_text=_('This field expects valid HTML. Entities must be '
                    'properly escaped.'),
        widget=ListEditWidgetWithClearButton(attrs={'size': 100}, sep='\n'))
    tips_file = forms.FileField(
        required=False,
        help_text=_('Load tips file. One line per tip. '
                    'This field expects valid text file. '
                    'If using HTML it must be properly escaped.'))
    def save(self):
        if not self.errors:
            smart_bytes_message = smart_bytes(self.cleaned_data['message'])
            smart_bytes_tips = smart_bytes(self.cleaned_data['tips'])
            self.siteconfig.set(
                'message_id',
                hashlib.sha256(smart_bytes_message).hexdigest())
            self.siteconfig.set(
                'tip_id',
                hashlib.sha256(smart_bytes_tips).hexdigest())

        super(MotdSettingsForm, self).save(extra_save_blacklist=['tips_file'])
