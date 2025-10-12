#!/bin/bash
cd ./services/
docker compose exec dns sh -c "s6-svc -r /run/service/dnsmasq"