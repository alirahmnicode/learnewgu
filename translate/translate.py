import requests
from bs4 import BeautifulSoup
from .constant import BASE_URL
from .constant import GOOGLE_LANGUAGES_TO_CODES as gls
from .exceptions import TranslationNotFound, TooManyRequests, RequestError
from .exceptions import LanguageNotSupportedException
from .constant import GOOGLE_LANGUAGES_TO_CODES as gls


class BaseTranslate:
    def __init__(self, text: str, target: str, source: str):
        self.text = text
        self.source = source
        self._check_language_support(target=target)

    def _check_language_support(self, target: str):
        """
        check if target language supported or not
        """
        if target in gls.values():
            self.target = target
        else:
            raise LanguageNotSupportedException(target)

    
class GoogleTranslate(BaseTranslate):
    """
    use google for translate
    """
    def __init__(self, text: str = "", target: str = "en", source: str = "auto"):
        self.element_tag = "div",
        self.element_query = {"class": "t0"},
        self._alt_element_query = {"class": "result-container"}
        super().__init__(text, target, source)

    def translate(self):
        response = requests.get(url=BASE_URL, params=self.get_params())

        if response.status_code == 429:
            raise TooManyRequests()

        if response.status_code != 200:
            raise RequestError()

        soup = BeautifulSoup(response.text, 'html.parser')

        element = soup.find(self.element_tag, self.element_query)
        
        if not element:
            element = soup.find(self.element_tag, self._alt_element_query)
            if not element:
                raise TranslationNotFound(self.text)
        return element.get_text(strip=True)

    def get_params(self):
        text = self.text.strip()
        params = dict()
        params['tl'] = self.target
        params['sl'] = self.source
        params['q'] = text
        return params

    def _is_language_supported(self, language: str):
        if language in gls.values() or language in gls.keys():
            return True
        else:
            return False

