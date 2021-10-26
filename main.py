import json
import sys
from argparse import ArgumentParser
from os.path import splitext
from typing import Set
from urllib.request import Request, urlopen
from urllib.error import HTTPError

URL_BASE = 'https://raw.githubusercontent.com/github/gitignore/master/'
GITHUB_API_URL = 'https://api.github.com/repos/github/gitignore/contents/'
OUT_FILE = '.gitignore'

parser = ArgumentParser(add_help=True)
parser.add_argument(
    '-l', action='store', dest='language', help='The language of the gitignore rules to include.'
)
parser.add_argument(
    '--list', action='store_true', dest='list', help='List available gitignore files in the repository'
)


def main():
    results = parser.parse_args()
    if results.list is True:
        for lang in get_available_gitignores():
            print(lang)
        sys.exit(0)
    if results.language is not None:
        get_remote_gitignore(language=results.language)


def parse_langs_from_json(*, resp: bytes) -> Set[str]:
    languages: Set[str] = set()
    for row in json.loads(resp):
        lang, extension = splitext(row['name'])
        if extension == '.gitignore':
            languages.add(lang)
    return languages


def get_available_gitignores() -> Set[str]:
    resp = github_http_request(url=GITHUB_API_URL)
    return parse_langs_from_json(resp=resp)


def get_remote_gitignore(*, out_file: str = OUT_FILE, language: str) -> None:
    """
    Queries the remote github/gitignore repository for gitignore rules and outputs
    them into a file of the users choice

    :param out_file: Name of output file to add Git ignore rules to
    :param language: Name of the language whose rules are to be saved

    :return None
    """
    # casefold() and capitalize() as all file names are capitalized in remote repository
    if not language:
        raise ValueError('--language cannot be empty')
    lang = language.casefold().capitalize()
    url = f'{URL_BASE}{lang}.gitignore'

    response = github_http_request(url=url, lang=lang)

    if response:
        with open(out_file, 'w+') as file:
            file.write(response.decode('utf-8'))


def github_http_request(*, url: str, lang: str = None) -> bytes:
    try:
        req = Request(url)
        response = urlopen(req)
        return response.read()
    except HTTPError as e:
        if hasattr(e, 'reason') and e.reason == 'Not Found':
            print(f'{e.code}: Couldn\'t find the gitignore file {lang} in the repository.')
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()