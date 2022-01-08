import requests
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--pull", help="PR Number ${{ github.event.number }}")
args = parser.parse_args()

response = requests.get(
    f"https://api.github.com/repos/python-docs-tr/python-docs-tr/pulls/{args.pull}/files"
)

response = json.loads(response.text)

for number in range(len(response)):
    print(response[number]["filename"])
