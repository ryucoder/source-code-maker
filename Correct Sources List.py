

Correct ones:

MRO count 2
ContextMixin Correct
DayMixin Correct
DeletionMixin Correct
MonthMixin Correct
TemplateResponseMixin Correct
WeekMixin Correct
YearMixin Correct
DateMixin Correct

MRO count 3
FormMixin Correct
SingleObjectMixin Correct
MultipleObjectMixin Correct
SingleObjectTemplateResponseMixin Correct
MultipleObjectTemplateResponseMixin Correct


MRO count 5
ModelFormMixin Correct


# from django.core.paginator import Paginator


# need to check in the mro properly
# from django.core.paginator import Page 



Issues to solve: 

1. If an attributes or code is written in between methods 
it is not shown in SCM.

E.g. HttpResponse 

if six.PY3:
    __bytes__ = serialize
else:
    __str__ = serialize


2. HttpResponseBase not shown in SCM

@property
def reason_phrase(self):
    if self._reason_phrase is not None:
        return self._reason_phrase
    # Leave self._reason_phrase unset in order to use the default
    # reason phrase for status code.
    return responses.get(self.status_code, 'Unknown Status Code')

@reason_phrase.setter
def reason_phrase(self, value):
    self._reason_phrase = value

@property
def charset(self):
    if self._charset is not None:
        return self._charset
    content_type = self.get('Content-Type', '')
    matched = _charset_from_content_type_re.search(content_type)
    if matched:
        # Extract the charset and strip its double quotes
        return matched.group('charset').replace('"', '')
    return settings.DEFAULT_CHARSET

@charset.setter
def charset(self, value):
    self._charset = value


if six.PY3:
    __bytes__ = serialize_headers
else:
    __str__ = serialize_headers

@property
def _content_type_for_repr(self):
    return ', "%s"' % self['Content-Type'] if 'Content-Type' in self else ''



__contains__ = has_header


3. HttpResponseRedirectBase

url = property(lambda self: self['Location'])


4. Queryset

as_manager.queryset_only = True
as_manager = classmethod(as_manager)


5. SCM for Paginator not working for SCM for Page and vice-versa 
Need a solution that works for every class



Patterns across issues :- 
1. getter, setter are not coming in SCM. (Hence deleter)            - Solved
2. Any attribute defined in between methods is not coming in SCM
3. Methods decorated with @cached_property is not coming in SCM.    - Solved
@cached_property is a class decorator








