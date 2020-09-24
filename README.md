# HCL Validator
Simple [HCL](https://github.com/hashicorp/hcl#hcl) validator for `*.tf` and `*.tfvars` files.

## Installation
```
$ sudo wget -O /usr/local/bin/hclvalidator https://raw.githubusercontent.com/mjaromi/hclvalidator/master/hclvalidator.py
$ sudo chmod +x /usr/local/bin/hclvalidator
```

## Usage
```
hclvalidator [PATH]
```
If `PATH` is ommitted then the tool will read from current (`.`) directory.

## Example
```
$ ls
variables.tfvars

$ cat variables.tfvars 
project_somevars = [
  { ENV_VAR_0 = "ENV_VAR_value_0" }
]

project_othervars = [
  { ENV_VAR_1 = "ENV_VAR_value_1" }
  { ENV_VAR_2 = "ENV_VAR_value_2" }
]

$ hclvalidator 
[./variables.tfvars] => [{ ENV_VAR_1 = "ENV_VAR_value_1" }] => [Line 7, column 121: unexpected LEFTBRACE; expected COMMA, IDENTIFIER, STRING, COMMENT, MULTICOMMENT, MINUS, NUMBER, FLOAT, $end, RIGHTBRACE, RIGHTBRACKET, RIGHTPAREN]
```
