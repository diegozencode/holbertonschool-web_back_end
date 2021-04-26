# 0x0B. Redis basic

# Description:bulb:

Redis is an open source, in memory data structure store, used as a database, cache, and message broker

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

## Technologies & Tools:computer:

[![Redis](https://img.shields.io/badge/≡-Redis-DC382D?&style=flat-square&logo=Redis&labelColor=282828)](https://redis.io/)
[![Git](https://img.shields.io/badge/≡-Git-F05032?logo=git&style=flat-square&labelColor=282828)](https://git-scm.com/)
[![Ubuntu](https://img.shields.io/badge/≡-Ubuntu-E95420?&style=flat-square&logo=Ubuntu&labelColor=282828)](https://ubuntu.com/)
[![GNU_Bash](https://img.shields.io/badge/≡-GNU_Bash-4EAA25?logo=GNU-Bash&style=flat-square&labelColor=282828)](https://www.gnu.org/software/bash/)
[![Vim](https://img.shields.io/badge/≡-Vim-019733?logo=Vim&style=flat-square&logoColor=019733&labelColor=282828)](https://www.vim.org/)
[![Vagrant](https://img.shields.io/badge/≡-Vagrant-1563FF?logo=vagrant&style=flat-square&logoColor=1563FF&labelColor=282828)](https://www.vagrantup.com/)
[![VS_Code](https://img.shields.io/badge/≡-VS_Code-007ACC?logo=visual-studio-code&style=flat-square&logoColor=007ACC&labelColor=282828)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/≡-Python-3776AB?logo=Python&style=flat-square&labelColor=282828)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/≡-GitHub-181717?logo=GitHub&style=flat-square&labelColor=282828)](https://github.com/)

---

## Resources:books:

Read or watch:

- [Redis commands](https://redis.io/commands)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

---

## Requirements:hammer:

- Ubuntu 18.04 LTS using python3 (version 3.7)
- Use pycodestyle (version 2.5)

### Install Redis on Ubuntu 18.04

```console
foo@pop-os:~$ sudo apt-get -y install redis-server
foo@pop-os:~$ pip3 install redis
foo@pop-os:~$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

---

### [0. Writing strings to Redis](./exercise.py)

### [1. Reading from Redis and recovering original type](./exercise.py)

### [2. Incrementing values](./exercise.py)

### [3. Storing lists](./exercise.py)

### [4. Retrieving lists](./exercise.py)

### [5. Implementing an expiring web cache and tracker](./web.py)

---

## Author

- **Diego Monroy** (@diegozencode) - [<img src="https://img.shields.io/badge/Portfolio-20d6fe.svg?&style=plastic"/>](https://diegozencode.me)
  [<img src="https://img.shields.io/badge/Twitter-1DA1F2.svg?&style=plastic&logo=twitter&logoColor=white"/>](https://twitter.com/diegozencode)
  [<img src="https://img.shields.io/badge/Linkedin-0A66C2.svg?&style=plastic&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/diegozencode)
  [<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=plastic&logo=github&logoColor=white"/>](https://github.com/diegozencode)
