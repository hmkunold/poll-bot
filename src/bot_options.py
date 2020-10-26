import argparse

deploy_parser = argparse.ArgumentParser('Specify options for bot deployment')
deploy_parser.add_argument('--restart', action='store_true', help='enables restart via discord commands')
