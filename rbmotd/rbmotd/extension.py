from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import TemplateHook


class MotdTemplateHook(TemplateHook):
    def __init__(self, extension):
        super(MotdTemplateHook, self).__init__(extension, 'base-after-navbar',
                                               'rbmotd/motd.html')

    def render_to_string(self, request, context):
        ext_settings = self.extension.settings

        context.update({
            'motd_close_value': '%s-closed' % ext_settings['message_id'],
            'motd_cookie': 'rbmotd',
            'motd_enabled': ext_settings.get('enabled'),
            'motd_message': ext_settings.get('message'),
            'motd_enabled_tips': ext_settings.get('enabled_tips'),
            'motd_tips': ext_settings.get('tips'),
            'motd_tip_close_value': '%s-closed' % ext_settings['tip_id'],
            'motd_tip_cookie': 'rbmotd_tip',
        })

        return super(MotdTemplateHook, self).render_to_string(request, context)

class MotdExtension(Extension):
    """Extends Review Board to display a Message of the Day.

    This allows an administrator to set announcement text that will appear at
    the top of every page. This can be used for important announcements,
    status updates, downtime notices, or anything else.
    """
    metadata = {
        'Name': 'Message of the Day',
        'Summary': (
            'Displays a configurable, dismissable announcement or message '
            'that will be shown to all Review Board users.'
        ),
    }

    css_bundles = {
        'default': {
            'source_filenames': ['css/motd.less'],
        }
    }

    js_bundles = {
        'motd_config': {
            'source_filenames': ['js/motd_tip.js'],
            'apply_to': ['reviewboard.extensions.views.configure_extension'],
        },
        'default': {
            'source_filenames': ['js/motd.js'],
        }
    }

    default_settings = {
        'enabled': False,
        'message': '',
        'message_id': '',
        'enabled_tips': False,
        'tips': '',
    }

    is_configurable = True

    def initialize(self):
        MotdTemplateHook(self)
