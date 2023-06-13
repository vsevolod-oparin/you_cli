#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.
import argparse
from pathlib import Path
import requests
import urllib.parse


PREFIX = 'how to use in linux CLI '


def get_file_content(token_path: Path) -> str:
    with open(token_path) as f:
        return f.read()


def get_response(query_text: str, api_key: str):
    safe_query_text = urllib.parse.quote_plus(query_text)
    url = f"https://api.betterapi.net/youchat?inputs={safe_query_text}&key={api_key}"
    try:
        json = requests.get(url).json()
    except:
        return "Something went wrong with API. Try another time."

    if json is not None and 'status_code' in json and json['status_code'] == 200:
        return json["generated_text"]
    else:
        if json is None:
            return "Error on API side. No response provided."
        elif 'status_code' in json:
            return "Error on API side. Reponse is malformed."
        else:
            return f"Error on API side. Code error is {json['status_code']}"


def get_parser():
    parser = argparse.ArgumentParser('You CLI tool to get requests to you.')
    parser.add_argument("--betterapi_key_path", default='betterapi', help="Path to betterapi API key")
    parser.add_argument('strings', nargs='+', type=str)
    return parser




def main() -> None:
    """Start the CLI."""
    args = get_parser().parse_args()
    betterapi_key = get_file_content(Path(args.betterapi_key_path))
    print(get_response(PREFIX + ' '.join(args.strings), api_key=betterapi_key))


if __name__ == "__main__":
    main()
