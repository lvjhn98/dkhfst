#!/bin/bash
from helpers.python import list_ips
import json

print(json.dumps(list_ips(), indent=4))