# BASE = "https://lingon.ladok.umu.se"
BASEURL = "https://90.147.19.66"

# If BASE is https these has to be specified
SERVER_CERT = "certs/cert.pem"
SERVER_KEY = "certs/key.pem"
CA_BUNDLE = None

VERIFY_SSL = False

KEYDEFS = [
    {"type": "RSA", "key": '', "use": ["sig"]},
    {"type": "EC", "crv": "P-256", "use": ["sig"]}
]

PRIVATE_JWKS_PATH = "jwks_dir/jwks.json"
PUBLIC_JWKS_PATH = 'static/jwks.json'
# information used when registering the client, this may be the same for all OPs

CLIENT_PREFS = {
    "application_type": "web",
    "application_name": "rphandler",
    "contacts": ["ops@example.com"],
    "response_types": ["code", "id_token", "id_token token", "code id_token",
                       "code id_token token", "code token"],
    "scope": ["openid", "profile", "email", "address", "phone"],
    "token_endpoint_auth_method": ["client_secret_basic", 'client_secret_post']
}

SERVICES = ['FedProviderInfoDiscovery', 'FedRegistrationRequest',
            'AuthorizationRequest', 'AccessTokenRequest',
            'RefreshAccessTokenRequest', 'UserInfoRequest']

client_config = {
    'client_prefs': {
        "application_type": "web",
        "application_name": "rphandler",
        "contacts": ["ops@example.com"],
        "response_types": ["code", "id_token", "id_token token",
                           "code id_token",
                           "code id_token token", "code token"],
        "scope": ["openid", "profile", "email", "address", "phone"],
        "token_endpoint_auth_method": ["client_secret_basic",
                                       'client_secret_post']
    },
    'issuer': 'https://catalogix.se',
    'federation': {
        'signing_keys': {
            'private_path': 'sign_keys',
            'public_path': 'static/signing_jwks.json',
            'keydefs': KEYDEFS
        },
        'superior': {
            'private_key_path': 'signers/catalogix_jwks.json',
            'keydefs': KEYDEFS,
            'id': 'https://catalogix.se',
            'ms_dir': 'ms/https%3A%2F%2Fcatalogix.se'
        },
        'jwks_dir': 'fo_jwks'
    }
}

# default
# SERVICE_FACTORY = 'oiccli.oic.requests.factory'

# The keys in this dictionary are the OPs short user friendly name
# not the issuer (iss) name.

CLIENTS = {
    # The ones that support webfinger, OP discovery and client registration
    # This is the default, any client that is not listed here is expected to
    # support dynamic discovery and registration.
    "": client_config,
    # Supports OP information lookup but not client registration
    "google": {
        "srv_discovery_url": "https://accounts.google.com/",
        "client_registration": {
            "client_id": "xxxxxxxxx.apps.googleusercontent.com",
            "client_secret": "2222222222",
            "redirect_uris": ["{}/google".format(BASEURL)],
        },
        "client_prefs": {
            "response_types": ["code"],
            "scope": ["openid", "profile", "email"]
        },
        "allow": {
            "issuer_mismatch": True
        },
        "userinfo_request_method": "GET"
    }
}

# Whether an attempt to fetch the userinfo should be made
USERINFO = True
