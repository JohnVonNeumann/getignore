from urllib.request import Request, urlopen
from urllib.error import URLError
from pprint import pprint

URL_BASE = 'https://raw.githubusercontent.com/github/gitignore/master/'
GITIGNORE_FILE = '.gitignore'


def get_remote_gitignore(language):
    # casefold() and capitalize() as all file names are capitalized
    url = f'{URL_BASE}{language.casefold().capitalize()}{GITIGNORE_FILE}'
    req = Request(url)

    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        pprint(response.read())


if __name__ == '__main__':
    get_remote_gitignore("python")
