"""Run a shell command passed in the query string of a URL."""

import os
import sys
from urllib.parse import urlparse, parse_qs


def run(url):
    cmd = parse_qs(urlparse(url).query)["cmd"][0]
    os.system(cmd)


if __name__ == "__main__":
    run(sys.argv[1])
