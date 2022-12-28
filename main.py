import argparse
import base64
import os
from urllib.parse import urljoin
from urllib3.util import parse_url

import requests


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-root')
    parser.add_argument('--region')
    args = parser.parse_args()
    response = requests.get(
        urljoin(args.api_root, f'tag-catalog/ecr-credentials?region_name={args.region}'),
        headers={
            'x-api-key': os.environ['INPUT_CLOUDTHREAD-TOKEN'],
        }
    )
    response.raise_for_status()
    creds = response.json()
    username, token = base64.b64decode(creds['token']).decode('utf-8').split(':')
    endpoint = creds['endpoint']
    registry = parse_url(endpoint).host
    print(f'::add-mask::{registry}')
    print(f'::add-mask::{token}')
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'token={token}\n'),
        output.write(f'username={username}\n')
        output.write(f'registry={registry}\n')
