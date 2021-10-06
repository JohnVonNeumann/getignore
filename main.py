from urllib.request import Request, urlopen
from urllib.error import URLError
from pprint import pprint

URL_BASE = 'https://raw.githubusercontent.com/github/gitignore/master/'
GITIGNORE_FILE = '.gitignore'
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_remote_gitignore(language):
    url = f'{URL_BASE}{language}{GITIGNORE_FILE}'
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_remote_gitignore("python")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
