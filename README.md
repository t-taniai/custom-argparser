# custom-argparser
Let `argparse` define acceptable arguments via external JSON files and overwrite them via command line.

# Usage
## Define the acceptable arguments via a JSON file
Define the argument names, their default values & types, choices (if needed), and help texts in the following formats.

- Scalar parameter: `"PARAM_NAME": [DEFAULT_VALUE, "HELPER_TEXT"]`
  - Define a scalar value parameter with its type (int, float, bool, or str) guessed from the default value.
- List parameter: `"PARAM_NAME": [[DEFAULT_VALUE, ..., DEFAULT_VALUE], "HELPER_TEXT"]`
  - Define a list of scalar value parameters with its type (int, float, bool, or str) guessed from the first default value.
- Categorical parameter: `"PARAM_NAME": [DEFAULT_VALUE, [CHOICE_1, CHOICE_2, ..., CHOICE_N], "HELPER_TEXT"]`
  - Define a scalar parameter with categorical choices. 
- Boolean flag parameter: `"PARAM_NAME": ["store_true", "HELPER_TEXT"]`
  - Define a boolean flag parameter, which is set to False as default and enabled by executing with `--PARAM_NAME`.

An example JSON file:

```json
{
    "name": ["resnet", "an example of string type argument."],
    "seed": [123, "an example of integer type argument."],
    "lr": [0.0002, "an example of float type argument."],
    "data_augment": [true, "an example of bool type argument."],
    "datasets": [["dataset1", "dataset2"], "an example of list of strings argument."],
    "image_size": [[320, 720], "an example of list of integers argument."],
    "layer_dims": [[32], "an example of possibly plural integer argument."],
    "activation": ["gelu", ["gelu", "relu", "leaky"], "an example of categorical string type argument."],
    "test_only": ["store_true", "an example of boolean flag argument."],
}
```


## Call get_options() in your python script 
```python
import custom_argparser

if __name__ == '__main__':
    args = custom_argparser.get_options()
    # Read argument values by accessing the attributes of args.
    print(args.name)
    print(args.seed)
    print(args.test_only)
    print(args.image_size[0], args.image_size[1])
```


## Run your python script by specifying the JSON file and overwritten parameters if needed
Run with the pre-defined parameters specified in the JSON file:
```bash
python demo.py --param_file default.json
# resnet
# 123
# False
# 320 720
```

Run with the pre-defined parameters as default values while overwriting some values:
```bash
python demo.py --param_file default.json --seed 0 --test_only --image_size 160 360
# resnet
# 0
# True
# 160 360
```

Note the script automatically tries to find `param_file` in ./params directory if the specified file does not exist.

---
Copyright (c) 2023 OMRON SINIC X Corporation and Tatsunori Taniai