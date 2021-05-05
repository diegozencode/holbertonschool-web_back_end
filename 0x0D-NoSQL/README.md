# 0x0D. NoSQL

## Description:bulb:

Introduction to NoSQL

- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Technologies & Tools:computer:

[![Git](https://img.shields.io/badge/≡-Git-F05032?logo=git&style=flat-square&labelColor=282828)](https://git-scm.com/)
[![Ubuntu](https://img.shields.io/badge/≡-Ubuntu-E95420?&style=flat-square&logo=Ubuntu&labelColor=282828)](https://ubuntu.com/)
[![GNU_Bash](https://img.shields.io/badge/≡-GNU_Bash-4EAA25?logo=GNU-Bash&style=flat-square&labelColor=282828)](https://www.gnu.org/software/bash/)
[![MongoDB](https://img.shields.io/badge/≡-MongoDB-47A248?logo=MongoDB&style=flat-square&labelColor=282828)](https://www.mongodb.com/)
[![Vim](https://img.shields.io/badge/≡-Vim-019733?logo=Vim&style=flat-square&logoColor=019733&labelColor=282828)](https://www.vim.org/)
[![Vagrant](https://img.shields.io/badge/≡-Vagrant-1563FF?logo=vagrant&style=flat-square&logoColor=1563FF&labelColor=282828)](https://www.vagrantup.com/)
[![VS_Code](https://img.shields.io/badge/≡-VS_Code-007ACC?logo=visual-studio-code&style=flat-square&logoColor=007ACC&labelColor=282828)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/≡-Python-3776AB?logo=Python&style=flat-square&labelColor=282828)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/≡-GitHub-181717?logo=GitHub&style=flat-square&labelColor=282828)](https://github.com/)

---

## Resources:books:

Read or watch:

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [Building Your First Application: An Introduction to MongoDB](https://www.youtube.com/watch?v=ClAQEARNUoQ)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/)
- [The mongo Shell](https://docs.mongodb.com/manual/mongo/)

---

## Requirements:hammer:

- Ubuntu 18.04 LTS using `MongoDB` (version 4.4)
- `python3` (version 3.7)
- `PyMongo` (version 3.11)
- `pycodestyle` style (version 2.5.\*)

### How to install MongoDB 4.4 in Ubuntu 18.04

```console
foo@pop-os:~$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
OK
foo@pop-os:~$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse
foo@pop-os:~$ sudo apt-get update
foo@pop-os:~$ sudo apt-get install -y mongodb-org
```

### Check status, start, stop and restart Mongo DB

```console
foo@pop-os:~$ sudo systemctl start mongod
foo@pop-os:~$ mongo --version
foo@pop-os:~$ sudo systemctl status mongod
foo@pop-os:~$ sudo systemctl stop mongod
foo@pop-os:~$ sudo systemctl restart mongod
```

### Install pymongo

```console
(python-env) foo@pop-os:~$ pip install pymongo
(python-env) foo@pop-os:~$ python
>>> import pymongo
>>> pymongo.__version__
'3.11.4'
```

---

## Files:card_file_box:
### [0. List all databases](./0-list_databases)

### [1. Create a database](./1-use_or_create_database)

### [2. Insert document](./2-insert)

### [3. All documents](./3-all)

### [4. All matches](./4-match)

### [5. Count](./5-count)

### [6. Update](./6-update)

### [7. Delete by match](./7-delete)

### [8. List all documents in Python](./8-all.py)

### [9. Insert a document in Python](./9-insert_school.py)

### [10. Change school topics](./10-update_topics.py)

### [11. Where can I learn Python?](./11-schools_by_topic.py)

### [12. Log stats](./12-log_stats.py)

### [13. Regex filter](./100-find)

### [14. Top students](./101-students.py)

### [12. Log stats - new version](./102-log_stats.py)

---

## Author

- **Diego Monroy** (@diegozencode) - [<img src="https://img.shields.io/badge/Portfolio-20d6fe.svg?&style=plastic"/>](https://diegozencode.me)
  [<img src="https://img.shields.io/badge/Twitter-1DA1F2.svg?&style=plastic&logo=twitter&logoColor=white"/>](https://twitter.com/diegozencode)
  [<img src="https://img.shields.io/badge/Linkedin-0A66C2.svg?&style=plastic&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/diegozencode)
  [<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=plastic&logo=github&logoColor=white"/>](https://github.com/diegozencode)
