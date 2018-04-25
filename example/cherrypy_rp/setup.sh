#!/usr/bin/env bash

if [ ! -f "fo/https%3A%2F%2Fedugain.org%2F.json" ]
then
    create_jwks.py > fo/https%3A%2F%2Fedugain.org%2F.json
fi

if [ ! -f "fo/https%3A%2F%2Fswamid.sunet.se%2F.json" ]
then
    create_jwks.py > fo/https%3A%2F%2Fswamid.sunet.se%2F.json
fi

if [ ! -f "catalogix_jwks.json" ]
then
    create_jwks.py > catalogix_jwks.json
fi

make_req.py -j catalogix_jwks.json -r catalogix_registration.json > catalogix_reg_ms.json

packer.py -j fo/https%3A%2F%2Fedugain.org%2F.json -i https://edugain.org/ -r catalogix_reg_ms.json > sms/https%3A%2F%2Fcatalogix.se/registration/https%3A%2F%2Fedugain.org%2F
packer.py -j fo/https%3A%2F%2Fswamid.sunet.se%2F.json -i https://swamid.sunet.se/ -r catalogix_reg_ms.json > sms/https%3A%2F%2Fcatalogix.se/registration/https%3A%2F%2Fswamid.sunet.se%2F