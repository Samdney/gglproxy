#-*- coding: utf-8 -*-

import argparse

def setArgParser():
    desc = "Using cache and translate Google proxy to visit websites"
    parser = argparse.ArgumentParser(description=desc, add_help=True)    
    
    parser.add_argument("-u", "--url", help="set the website url to visit")
    
    subparsers = parser.add_subparsers(title="proxy_name", dest="proxy_version")
    subparsers.add_parser("cache", help="google's cache proxy")
    subparsers.add_parser("translate", help="google's translate proxy")
    
    parser.add_argument("-lf", "--lang-from", help="set the origin language {de, en, fr, jp, ...}. Default: en")
    parser.add_argument("-lt", "--lang-to", help="set the target language {de, en, fr, jp, ...}. Default: en")
    
    #parser.add_argument('-br', '--open-webbrowser', action='store_true', default=False, help='open proxy link in webbrowser')
    
    return parser
