#!/bin/bash
cd ./services/ 
docker compose cp caddy:/data/caddy/pki/authorities/local/root.crt ${DKHFST_DATA_DIR}/common/ca.crt
