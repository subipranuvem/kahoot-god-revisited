import sys
from urllib.parse import urlparse


class URLChooser:
    @classmethod
    def choose_url(cls) -> str:
        args_len = len(sys.argv)
        no_url_informed = args_len == 1
        not_expected_args = args_len > 2
        if not_expected_args:
            raise ValueError("more than 1 arg informed")
        if no_url_informed:
            return cls._get_url_from_input()
        url = sys.argv[1]
        if not cls._is_a_valid_url(url):
            raise ValueError("invalid url")
        return url

    @classmethod
    def _get_url_from_input(cls) -> str:
        url = input("Enter the quiz URL: ")
        is_a_valid_url = False
        while not is_a_valid_url:
            if cls._is_a_valid_url(url):
                is_a_valid_url = True
            else:
                url = input("Invalid URL, try another URL: ")
        return url

    @classmethod
    def _is_a_valid_url(cls, url: str) -> str:
        result = urlparse(url)
        return result.scheme and result.netloc
