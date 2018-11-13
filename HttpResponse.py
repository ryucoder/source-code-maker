'''
****************************************
Location of the Class HttpResponse : django.http.response
****************************************
'''

class HttpResponse(HttpResponseBase):

    streaming  =  False


    status_code  =  200


    def __init__(self, content_type=None, status=None, reason=None, charset=None):
        # _headers is a mapping of the lower-case name to the original case of
        # the header (required for working with legacy systems) and the header
        # value. Both the name of the header and its value are ASCII strings.
        self._headers = {}
        self._closable_objects = []
        # This parameter is set by the handler. It's necessary to preserve the
        # historical behavior of request_finished.
        self._handler_class = None
        self.cookies = SimpleCookie()
        self.closed = False
        if status is not None:
            try:
                self.status_code = int(status)
            except (ValueError, TypeError):
                raise TypeError('HTTP status code must be an integer.')

            if not 100 <= self.status_code <= 599:
                raise ValueError('HTTP status code must be an integer from 100 to 599.')
        self._reason_phrase = reason
        self._charset = charset
        if content_type is None:
            content_type = '%s; charset=%s' % (settings.DEFAULT_CONTENT_TYPE,
                                               self.charset)
        self['Content-Type'] = content_type

    def __init__(self, content=b'', *args, **kwargs):
        super(HttpResponse, self).__init__(*args, **kwargs)
        # Content is a bytestring. See the `content` property methods.
        self.content = content

    def __repr__(self):
        return '<%(cls)s status_code=%(status_code)d%(content_type)s>' % {
            'cls': self.__class__.__name__,
            'status_code': self.status_code,
            'content_type': self._content_type_for_repr,
        }

    def getvalue(self):
        return self.content

    def serialize(self):
        """Full HTTP message, including headers, as a bytestring."""
        return self.serialize_headers() + b'\r\n\r\n' + self.content

    def tell(self):
        return len(self.content)

    def writable(self):
        return True

    def write(self, content):
        self._container.append(self.make_bytes(content))

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def _convert_to_charset(self, value, charset, mime_encode=False):
        """Converts headers key/value to ascii/latin-1 native strings.

        `charset` must be 'ascii' or 'latin-1'. If `mime_encode` is True and
        `value` can't be represented in the given charset, MIME-encoding
        is applied.
        """
        if not isinstance(value, (bytes, six.text_type)):
            value = str(value)
        if ((isinstance(value, bytes) and (b'\n' in value or b'\r' in value)) or
                isinstance(value, six.text_type) and ('\n' in value or '\r' in value)):
            raise BadHeaderError("Header values can't contain newlines (got %r)" % value)
        try:
            if six.PY3:
                if isinstance(value, str):
                    # Ensure string is valid in given charset
                    value.encode(charset)
                else:
                    # Convert bytestring using given charset
                    value = value.decode(charset)
            else:
                if isinstance(value, str):
                    # Ensure string is valid in given charset
                    value.decode(charset)
                else:
                    # Convert unicode string to given charset
                    value = value.encode(charset)
        except UnicodeError as e:
            if mime_encode:
                # Wrapping in str() is a workaround for #12422 under Python 2.
                value = str(Header(value, 'utf-8', maxlinelen=sys.maxsize).encode())
            else:
                e.reason += ', HTTP response headers must be in %s format' % charset
                raise
        return value

    def close(self):
        for closable in self._closable_objects:
            try:
                closable.close()
            except Exception:
                pass
        self.closed = True
        signals.request_finished.send(sender=self._handler_class)

    def delete_cookie(self, key, path='/', domain=None):
        self.set_cookie(key, max_age=0, path=path, domain=domain,
                        expires='Thu, 01-Jan-1970 00:00:00 GMT')

    def flush(self):
        pass

    def get(self, header, alternate=None):
        return self._headers.get(header.lower(), (None, alternate))[1]

    def has_header(self, header):
        """Case-insensitive check for a header."""
        return header.lower() in self._headers

    def items(self):
        return self._headers.values()

    def make_bytes(self, value):
        """Turn a value into a bytestring encoded in the output charset."""
        # Per PEP 3333, this response body must be bytes. To avoid returning
        # an instance of a subclass, this function returns `bytes(value)`.
        # This doesn't make a copy when `value` already contains bytes.

        # Handle string types -- we can't rely on force_bytes here because:
        # - under Python 3 it attempts str conversion first
        # - when self._charset != 'utf-8' it re-encodes the content
        if isinstance(value, bytes):
            return bytes(value)
        if isinstance(value, six.text_type):
            return bytes(value.encode(self.charset))

        # Handle non-string types (#16494)
        return force_bytes(value, self.charset)

    def readable(self):
        return False

    def seekable(self):
        return False

    def serialize_headers(self):
        """HTTP headers as a bytestring."""
        def to_bytes(val, encoding):
            return val if isinstance(val, bytes) else val.encode(encoding)

        headers = [
            (b': '.join([to_bytes(key, 'ascii'), to_bytes(value, 'latin-1')]))
            for key, value in self._headers.values()
        ]
        return b'\r\n'.join(headers)

    def set_cookie(self, key, value='', max_age=None, expires=None, path='/',
                   domain=None, secure=False, httponly=False):
        """
        Sets a cookie.

        ``expires`` can be:
        - a string in the correct format,
        - a naive ``datetime.datetime`` object in UTC,
        - an aware ``datetime.datetime`` object in any time zone.
        If it is a ``datetime.datetime`` object then ``max_age`` will be calculated.
        """
        value = force_str(value)
        self.cookies[key] = value
        if expires is not None:
            if isinstance(expires, datetime.datetime):
                if timezone.is_aware(expires):
                    expires = timezone.make_naive(expires, timezone.utc)
                delta = expires - expires.utcnow()
                # Add one second so the date matches exactly (a fraction of
                # time gets lost between converting to a timedelta and
                # then the date string).
                delta = delta + datetime.timedelta(seconds=1)
                # Just set max_age - the max_age logic will set expires.
                expires = None
                max_age = max(0, delta.days * 86400 + delta.seconds)
            else:
                self.cookies[key]['expires'] = expires
        else:
            self.cookies[key]['expires'] = ''
        if max_age is not None:
            self.cookies[key]['max-age'] = max_age
            # IE requires expires, so set it if hasn't been already.
            if not expires:
                self.cookies[key]['expires'] = cookie_date(time.time() +
                                                           max_age)
        if path is not None:
            self.cookies[key]['path'] = path
        if domain is not None:
            self.cookies[key]['domain'] = domain
        if secure:
            self.cookies[key]['secure'] = True
        if httponly:
            self.cookies[key]['httponly'] = True

    def set_signed_cookie(self, key, value, salt='', **kwargs):
        value = signing.get_cookie_signer(salt=key + salt).sign(value)
        return self.set_cookie(key, value, **kwargs)

    def setdefault(self, key, value):
        """Sets a header unless it has already been set."""
        if key not in self:
            self[key] = value

