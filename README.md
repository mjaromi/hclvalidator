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
  { DB_NAME="db_xyz" },
]

project_othervars = [
  { DB_NAME = "db_dev_project-adapter" },
  { DB_USER = "db_dev_project-adapter" },
  { SERVICE_8080_NAME  = "project-adapter" },
  { SERVICE_8080_TAGS = "extecs-gw" },
  { SERVICE_8081_NAM}  = "project-adapter" },
  { SERVICE_8081_TAGS = "extecs-gw,status" }
]

$ hclvalidator 
[./variables.tfvars] => [{ SERVICE_8081_NAM}  = "project-adapter" },] => [Line 10, column 259: unexpected RIGHTBRACE; expected EQUAL, COLON, LEFTBRACE, COMMENT, MULTICOMMENT, IDENTIFIER, STRING, MINUS, NUMBER, FLOAT]
```
