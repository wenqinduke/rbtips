from __future__ import unicode_literals

from django.forms.util import flatatt
from django.template.context import Context
from django.template.loader import render_to_string

from django.utils.six.moves import filter
from django.utils.translation import ugettext as _

from djblets.forms.widgets import ListEditWidget


class ListEditWidgetWithClearButton(ListEditWidget):
    template_name = 'rbmotd/list_edit_widget_with_clear_button.html'
    