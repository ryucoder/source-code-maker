
Update read me on how to ad more magic methods 

1.

__setitem__
__delitem__
__getitem__

__deepcopy__
__getstate__
__setstate__
__len__
__bool__
__nonzero__
__and__
__or__

ALLOWED_MAGIC_METHODS = []




Wrong ones : 
1. DateMixin 
    @cached_property
    def uses_datetime_field(self):


3. If an attributes or code is written in between methods 
it is not shown in SCM.

E.g. HttpResponse 

if six.PY3:
    __bytes__ = serialize
else:
    __str__ = serialize


4. Below code from HttpResponse is not coming in SCM
 
@property
def content(self):
    return b''.join(self._container)

@content.setter
def content(self, value):



5. HttpResponseBase not shown in SCM

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


6. HttpResponseRedirectBase

url = property(lambda self: self['Location'])


9 . Paginator 

@cached_property
def count(self):
    
@cached_property
def num_pages(self):

@property
def page_range(self):

10. Queryset

as_manager.queryset_only = True
as_manager = classmethod(as_manager)















Correct ones : 

MRO count 1
ContextMixin Correct
DayMixin Correct
DeletionMixin Correct
MonthMixin Correct
TemplateResponseMixin Correct
WeekMixin Correct
YearMixin Correct


MRO count 3
FormMixin Correct
SingleObjectMixin Correct
MultipleObjectMixin Correct
SingleObjectTemplateResponseMixin Correct
MultipleObjectTemplateResponseMixin Correct


MRO count 5 
ModelFormMixin Correct







