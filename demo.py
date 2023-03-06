#
# Copyright (c) 2023 OMRON SINIC X Corporation and Tatsunori Taniai
# 

import custom_argparser

if __name__ == '__main__':
    args = custom_argparser.get_options()
    # Read argument values by accessing the attributes of args.
    print(args.name)
    print(args.seed)
    print(args.test_only)
    print(args.image_size[0], args.image_size[1])
