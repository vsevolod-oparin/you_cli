#!/usr/bin/env python3
import argparse
from pathlib import Path
import requests
import urllib.parse

TEMPLATE = 'how to {} in Linux'


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
    parser.add_argument('strings', nargs='+', type=str)
    return parser


def main() -> None:
    """Start the CLI."""
    args = get_parser().parse_args()
    config_path = Path.home() / '.config' / 'you' / 'betterapi'
    betterapi_key = get_file_content(config_path)
    print(get_response(TEMPLATE.format(' '.join(args.strings)), api_key=betterapi_key))


if __name__ == "__main__":
    main()
