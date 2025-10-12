#!/bin/bash
sudo cp ${DKHFST_DATA_DIR}/caddy-pki/authorities/local/root.crt \
        ${DKHFST_DATA_DIR}/common/ca.crt 
sudo chmod 644 ${DKHFST_DATA_DIR}/common/ca.crt 
