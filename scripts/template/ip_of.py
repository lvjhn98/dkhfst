#!/bin/bash
from helpers.python import list_ips
import json
import sys

print(list_ips()[sys.argv[1]])