from argparse import ArgumentParser
from urllib.request import Request, urlopen
from urllib.error import URLError
from pprint import pprint

URL_BASE = 'https://raw.githubusercontent.com/github/gitignore/master/'
GITIGNORE_FILE = '.gitignore'

parser = ArgumentParser(add_help=True)
parser.add_argument(
    '-l', action='store', dest='language', help='The language of the gitignore rules to include.'
)

def get_remote_gitignore(language):
    # casefold() and capitalize() as all file names are capitalized
    lang = language.casefold().capitalize()
    url = f'{URL_BASE}{lang}{GITIGNORE_FILE}'
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
        with open(GITIGNORE_FILE, 'w+') as file:
            file.write(response.read().decode('utf-8'))


if __name__ == '__main__':
    results = parser.parse_args()
    if results.language is not None:
        get_remote_gitignore(results.language)
