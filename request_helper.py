from requests import Response, Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class RequestsHelper:
    """Requests abstaction class. Provides a fast *just works* implementation for HTTP requests."""

    session: Session

    def __init__(self, retry_strategy: dict = {}):
        """
        :param retry_strategy: dictionary of options for Retry
        """
        self.set_strategy(retry_strategy)

    def set_strategy(self, retry_strategy: dict = {}) -> None:
        """
        Updates the retry strategy
        :param retry_stragegy: dictionary of options for Retry
        """
        retry_opts = {"total": 5, "backoff_factor": 1}
        retry_opts.update(retry_strategy)

        http_addapter = HTTPAdapter(max_retries=Retry(**retry_opts))
        self.session = Session()
        self.session.mount("https://", http_addapter)

    def request(self, kwargs: dict) -> Response:
        """
        Dispatches a request
        :raises requests.exceptions: (see requests.Session.request)
        """
        return self.session.request(**kwargs)

    def get(self, url: str) -> Response:
        """
        Dispatches a GET request
        :raises requests.exceptions: (see requests.Session.get)
        """
        return self.session.get(url)

    def post(self, url: str, data: dict) -> Response:
        """
        Dispatches a POST request
        "raises requests.exceptions: (see requests.Session.post)
        """
        return self.session.post(url, data)

    def put(self, url: str, data: dict) -> Response:
        """
        Dispatches a PUT request
        :raises requests.exceptions: (see requests.Session.put)
        """
        return self.session.put(url, data)

    def delete(self, url: str) -> Response:
        """
        Dispatches a DELETE request
        :raises requests.exceptions: (see requests.Session.put)
        """
        return self.session.delete(url)

