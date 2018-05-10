#!/usr/bin/env python3
import importlib
import sys

from fedoidcmsg.entity import make_federation_entity


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='port', default=80, type=int)
    parser.add_argument(dest="config")
    args = parser.parse_args()

    sys.path.insert(0, ".")
    config = importlib.import_module(args.config)

    federation_entity = make_federation_entity(config.client_config['federation'], '')

    print('')