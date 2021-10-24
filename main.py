from argparse import ArgumentParser
from urllib.request import Request, urlopen
from urllib.error import URLError

URL_BASE = 'https://raw.githubusercontent.com/github/gitignore/master/'
OUT_FILE = '.gitignore'

parser = ArgumentParser(add_help=True)
parser.add_argument(
    '-l', action='store', dest='language', help='The language of the gitignore rules to include.'
)


def get_remote_gitignore(*, out_file=OUT_FILE, language) -> None:
    # casefold() and capitalize() as all file names are capitalized
    if not language:
        raise ValueError('--language cannot be empty')
    lang = language.casefold().capitalize()
    url = f'{URL_BASE}{lang}.gitignore'
    req = Request(url)

    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason') and e.reason == 'Not Found':
            print(f'{e.code}: Couldn\'t find the gitignore file {lang} in the repository.')
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        with open(out_file, 'w+') as file:
            file.write(response.read().decode('utf-8'))


if __name__ == '__main__':
    results = parser.parse_args()
    if results.language is not None:
        get_remote_gitignore(results.language)
