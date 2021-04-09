# 0x08. User authentication service

# Description:bulb:

Implement a user authentication service

"I changed all my passwords to 'incorrect'. So whenever I forget, it will tell me 'Your password is incorrect.'"

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Technologies & Tools:computer:

[![Ubuntu](https://img.shields.io/badge/≡-Ubuntu-E95420?&style=flat-square&logo=Ubuntu&labelColor=282828)](https://ubuntu.com/)
[![Git](https://img.shields.io/badge/≡-Git-F05032?logo=git&style=flat-square&labelColor=282828)](https://git-scm.com/)
[![GNU_Bash](https://img.shields.io/badge/≡-GNU_Bash-4EAA25?logo=GNU-Bash&style=flat-square&labelColor=282828)](https://www.gnu.org/software/bash/)
[![Vim](https://img.shields.io/badge/≡-Vim-019733?logo=Vim&style=flat-square&logoColor=019733&labelColor=282828)](https://www.vim.org/)
[![Vagrant](https://img.shields.io/badge/≡-Vagrant-1563FF?logo=vagrant&style=flat-square&logoColor=1563FF&labelColor=282828)](https://www.vagrantup.com/)
[![VS_Code](https://img.shields.io/badge/≡-VS_Code-007ACC?logo=visual-studio-code&style=flat-square&logoColor=007ACC&labelColor=282828)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/≡-Python-3776AB?logo=Python&style=flat-square&labelColor=282828)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/≡-GitHub-181717?logo=GitHub&style=flat-square&labelColor=282828)](https://github.com/)
[![Flask](https://img.shields.io/badge/≡-Flask-000000?logo=Flask&style=flat-square&labelColor=282828)](https://flask.palletsprojects.com/en/1.1.x/)

---

## Resources:books:

Read or watch:

- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Requests module](https://requests.kennethreitz.org/en/master/user/quickstart/)
- [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

---

## Requirements:hammer:

- Ubuntu 18.04 LTS using python3 (version 3.7)
- Use pycodestyle (version 2.5)

### Install bcrypt

```bash
pip3 install bcrypt
```

---

### [0. User model](./user.py)

### [1. create user](./db.py)

### [2. Find user](./db.py)

### [3. update user](./db.py)

### [4. Hash password](./auth.py)

### [5. Register user](./auth.py)

### [6. Basic Flask app](./app.py)

### [7. Register user](./app.py)

### [8. Credentials validation](./auth.py)

### [9. Generate UUIDs](./auth.py)

### [10. Get session ID](./auth.py)

### [11. Log in](./app.py)

### [12. Find user by session ID](./auth.py)

### [13. Destroy session](./auth.py)

### [14. Log out](./app.py)

### [15. User profile](./app.py)

### [16. Generate reset password token](./auth.py)

### [17. Get reset password token](./app.py)

### [18. Update password](./auth.py)

### [19. Update password end-point](./app.py)

---

## Author

- **Diego Monroy** (@diegozencode) - [<img src="https://img.shields.io/badge/Portfolio-20d6fe.svg?&style=plastic"/>](https://diegozencode.me)
  [<img src="https://img.shields.io/badge/Twitter-1DA1F2.svg?&style=plastic&logo=twitter&logoColor=white"/>](https://twitter.com/diegozencode)
  [<img src="https://img.shields.io/badge/Linkedin-0A66C2.svg?&style=plastic&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/diegozencode)
  [<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=plastic&logo=github&logoColor=white"/>](https://github.com/diegozencode)
