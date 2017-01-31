import requests_mock
import logging

from .sessions import MockedSessionsMixin
from .licenses import MockedLicensesMixin
from .shorturl import MockedShortUrlMixin
from .csrf import MockedCsrfMixin
from .uiquery import MockedUIQueryMixin

from loginsightexport.uidriver import Connection, Credentials

mockserverlogger = logging.getLogger("LogInsightMockAdapter")

requests_mock.mock.case_sensitive = True


class LogInsightMockAdapter(MockedUIQueryMixin, MockedShortUrlMixin, MockedLicensesMixin, MockedSessionsMixin, MockedCsrfMixin, requests_mock.Adapter):
    pass


class MockedConnection(Connection):
    """A regular loginsightexport.uidriver.Connection that has a LogInsightMockAdapter pre-mounted"""
    def __init__(self, *args, **kwargs):
        # no outbound requests are made during init
        super(MockedConnection, self).__init__(*args, **kwargs)

        # Mount the requests-mock-adapter
        adapter = LogInsightMockAdapter()
        self._requestsession.mount('https://', adapter)


def mock_server_with_authenticated_connection():
    """Instantiate a LogInsightMockAdapter with a """
    raise DeprecationWarning()
    connection = Connection("mockserverlocal", auth=Credentials("admin", "password", "mock"))
    adapter = LogInsightMockAdapter()
    adapter.prep()
    connection._requestsession.mount('https://', adapter)
    return connection


def mock_server_with_authenticated_connection_and_bad_credentials():
    raise DeprecationWarning()
    connection = Connection("mockserverlocal", auth=Credentials("fakeuserthatdoesntexist", "", "mock"))
    adapter = LogInsightMockAdapter()
    adapter.prep()
    connection._requestsession.mount('https://', adapter)
    return connection


def mock_server_with_connection_and_no_credentials():
    raise DeprecationWarning()
    connection = Connection("mockserverlocal", auth=None)
    adapter = LogInsightMockAdapter()
    adapter.prep()
    connection._requestsession.mount('https://', adapter)
    return connection