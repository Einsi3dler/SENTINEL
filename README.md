# Sentinel Project Documentation

## Introduction

Sentinel is your trusted partner in online transactions, serving as a secure escrow platform. Designed to eliminate uncertainties between buyers and sellers, Sentinel fosters a reliable environment where transactions can occur without the need for inherent trust. Beyond basic escrow services, Sentinel includes features such as maintaining a comprehensive database of verified scammers in online marketplaces and empowering users with the ability to create legally binding contracts.

## Key Features

- **Escrow Platform**: Facilitate secure transactions with a trusted intermediary.
- **Scammer Database**: Maintain a curated list of known scammers to protect users.
- **Contract Creation**: Empower users to draft and enforce agreements with ease.

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Info](#info)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

### 1. MySQL and MySQL Connector for Python (MySQLdb)

#### Installation

- **Linux**:
  ```bash
  sudo apt-get update
  sudo apt-get install mysql-server
  sudo mysql_secure_installation
  sudo apt-get install python3-dev libmysqlclient-dev
  pip install mysqlclient
  pip install sqlalchemy mysql-connector-python
 **Database Setup**:
  - Execute `setup_mysql_dev.sql` and `setup_mysql_test.sql` scripts to initialize databases.
  - Configure MySQL connection details in `Sentinel/models/engine/pass.json` and `Sentinel/models/engine/testpass.json`.

* Clone this repository
* Run Sentinel Console(interactively): `./console` and enter command
* Run Sentinel Console(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it and prints the id
* `destroy` - Deletes an instance based on the class name and id. 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute. 

## Examples of use
```
vagrantSentinel$./console.py
(Sentinel) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(Sentinel) all MyModel
** class doesn't exist **
(Sentinel) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(Sentinel) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(Sentinel) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(Sentinel) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(Sentinel) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(Sentinel) quit
```

## Bugs
No known bugs at this time. 

## Info
For inquiries or feedback, please reach out to Sylvester Divine at [sylvesterdivine@outlook.com](mailto:sylvesterdivine@outlook.com). We value your input and are committed to enhancing your transaction security experience with Sentinel. 
