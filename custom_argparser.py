#
# Copyright (c) 2023 OMRON SINIC X Corporation and Tatsunori Taniai
# 

import argparse
import json
from distutils.util import strtobool

"""
Usage:
    By executing
        python demo.py --param_file default.json
    the program loads default.json to define the arguments and their default values.
    Furthermore, one can manually specify these argument values. For example, changing
    seed to 0 can be done as follows.
        python demo.py --param_file default.json --seed 0
"""
def get_options():

    argparser = argparse.ArgumentParser(description='Custom argument parser')
    argparser.add_argument('-p', '--param_file', type=str, default='default.json', help='filename of the parameter JSON')
    args, unknown = argparser.parse_known_args()

    try:
        params = json.load(open(f'{args.param_file}'))
    except:
        params = json.load(open(f'./params/{args.param_file}'))

    # load the json config and use it as default values.
    boolder = lambda x:bool(strtobool(x))
    typefinder = lambda v: str if v is None else boolder if type(v)==bool else type(v)
    for key, val in params.items():
        vdef, help = val[0], val[-1]
        vt = typefinder(vdef)
        opt = {}
        if isinstance(vdef, (list, tuple)):
            opt['nargs'] = '+'
            vt = typefinder(vdef[0])
        if len(val) == 3:
            opt['choices'] = val[1]
        if vdef == 'store_true':
            argparser.add_argument(f"--{key}", action='store_true', help=help, **opt)
        else:
            argparser.add_argument(f"--{key}", type=vt, default=vdef, help=help, **opt)
    args = argparser.parse_args()
    argparser.print_help()
    return args
