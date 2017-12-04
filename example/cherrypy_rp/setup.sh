#!/usr/bin/env bash

#create_jwks.py > signers/edugain_jwks.json
#create_jwks.py > signers/catalogix_jwks.json

make_req.py -j signers/catalogix_jwks.json -r catalogix_registration.json > catalogix_reg_ms.json

packer.py -j signers/edugain.org_jwks.json -i https://edugain.org/ -r catalogix_reg_ms.json > ms/https%3A%2F%2Fcatalogix.se/registration/https%3A%2F%2Fedugain.org%2F
packer.py -j signers/swamid.sunet.se_jwks.json -i https://swamid.sunet.se/ -r catalogix_reg_ms.json > ms/https%3A%2F%2Fcatalogix.se/registration/https%3A%2F%2Fswamid.sunet.se%2F