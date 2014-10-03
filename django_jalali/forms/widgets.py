from django.forms import widgets
from django.utils.encoding import smart_str
from django.utils import formats
import time
import datetime
import jdatetime

class jDateInput(widgets.Input):
    input_type = 'text'
    format = None

    def __init__(self, attrs=None, format=None):
        super(jDateInput, self).__init__(attrs)
        if format:
            self.format = format

    def _format_value(self, value):
        if value is None:
            return ''
        elif hasattr(value, 'strftime'):
            f = smart_str(self.format or formats.get_format('DATE_INPUT_FORMATS')[0])
            return value.strftime(f)

        return value

    def render(self, name, value, attrs=None):
        value = self._format_value(value)
        return super(jDateInput, self).render(name, value, attrs)

    def _has_changed(self, initial, data):
        # If our field has show_hidden_initial=True, initial will be a string
        # formatted by HiddenInput using formats.localize_input, which is not
        # necessarily the format used for this widget. Attempt to convert it.
        try:
            input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
            initial = jdatetime.date(*time.strptime(initial, input_format)[:3])
        except (TypeError, ValueError):
            pass
        return super(jDateInput, self)._has_changed(self._format_value(initial), data)

class jDateTimeInput(widgets.Input):
    input_type = 'text'
    format = '%Y-%m-%d %H:%M:%S'     # '2006-10-25 14:30:59'

    def __init__(self, attrs=None, format=None):
        super(jDateTimeInput, self).__init__(attrs)
        if format:
            self.format = format
            self.manual_format = True
        else:
            self.format = formats.get_format('DATETIME_INPUT_FORMATS')[0]
            self.manual_format = False

    def _format_value(self, value):
        if self.is_localized and not self.manual_format:
            return formats.localize_input(value)
        elif hasattr(value, 'strftime'):
            value = datetime_safe.new_datetime(value)
            return value.strftime(self.format)
        return value

    def _has_changed(self, initial, data):
        # If our field has show_hidden_initial=True, initial will be a string
        # formatted by HiddenInput using formats.localize_input, which is not
        # necessarily the format used for this widget. Attempt to convert it.
        try:
            input_format = formats.get_format('DATETIME_INPUT_FORMATS')[0]
            initial = datetime.datetime(*time.strptime(initial, input_format)[:6])
        except (TypeError, ValueError):
            pass
        return super(jDateTimeInput, self)._has_changed(self._format_value(initial), data)

from django import forms
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
import datetime,time




calbtn = u'''<img src="/static/images/cal.png" alt="calendar" id="%s_btn"
style="cursor: pointer; width: 18px; height:18px; vertical-align:middle; float: none;" title="Select date" />
<script type="text/javascript">
    function onJalaliDateSelected(calendar, date) {
        var e = document.getElementById("%s");
        var str = calendar.date.getFullYear() + "-" + (calendar.date.getMonth()+1) + "-" + calendar.date.getDate();
        e.value = str;
    }
    Calendar.setup({
        inputField     :    "%s_display",
        button         :    "%s_btn",
        ifFormat       :    "%s",
        dateType       :    "jalali",
        weekNumbers    :     true,
        onUpdate       :     onJalaliDateSelected
    });
</script>'''

class DateTimeWidget(forms.widgets.TextInput):

    class Media:
        css = {
            'all': ('/static/css/calendar-system.css',)
        }
        js = (
              '/static/js/jalali.js',
              '/static/js/calendar.js',
              '/static/js/calendar-setup.js',
              '/static/js/lang/calendar-fa.js',
        )

    dformat = '%Y-%m-%d'
   #dformat = '%Y-%m-%d %H:%M:%S'


    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            try:
                final_attrs['value'] = \
                                   force_unicode(value.strftime(self.dformat))
            except:
                final_attrs['value'] = \
                                   force_unicode(value)
        if not final_attrs.has_key('id'):
            final_attrs['id'] = u'%s_id' % (name)
        id = final_attrs['id']

        jsdformat = self.dformat #.replace('%', '%%')
        cal = calbtn % (id, id, id, id, jsdformat)
        parsed_atts = forms.util.flatatt(final_attrs)
         #a = u'<span><input type="text" id="%s_display" value="%s"/><input type="hidden" %s/> %s%s</span>' % (id,dat_f, parsed_atts, self.media, cal)
        try:
            a = u'<span><input type="text" id="%s_display" value="%s" readonly/><input type="hidden"  %s/> %s%s</span>' % (id,final_attrs['value'],parsed_atts, self.media, cal)
        except KeyError:
            a = u'<span><input type="text" id="%s_display" readonly/><input type="hidden" %s/> %s%s</span>' % (id,parsed_atts, self.media, cal)
        #else:
        #    a = u'<span><input type="text" id="%s_display" readonly/><input type="hidden" %s/> %s%s</span>' % (id,parsed_atts, self.media, cal)
        #a = u'<span><input type="text" id="%s_display" readonly/><input type="text" %s/> %s%s</span>' % (id,parsed_atts, self.media, cal)
        return mark_safe(a)

    def value_from_datadict(self, data, files, name):
        from datetime import timedelta#one crazy error on js code and i can solve that! so i fix it here!!!
        dtf = formats.get_format('DATETIME_INPUT_FORMATS')
        empty_values = forms.fields.EMPTY_VALUES
        value = data.get(name, None)
        if value in empty_values:
            return None
        if isinstance(value, datetime.datetime):
            value = value + timedelta(days=1)
            return value
        if isinstance(value, datetime.date):
            value = value + timedelta(days=1)
            return datetime.datetime(value.year, value.month, value.day)
        for format in dtf:
            try:
                return datetime.datetime(*time.strptime(value, format)[:6]) + timedelta(days=1)
            except ValueError:
                continue
        return None

    def _has_changed(self, initial, data):
        """
        Return True if data differs from initial.
        Copy of parent's method, but modify value with strftime function before final comparsion
        """
        if data is None:
            data_value = u''
        else:
            data_value = data

        if initial is None:
            initial_value = u''
        else:
            initial_value = initial

        try:
            if force_unicode(initial_value.strftime(self.dformat)) != force_unicode(data_value.strftime(self.dformat)):
                return True
        except:
            if force_unicode(initial_value) != force_unicode(data_value):
                return True
        return False


