# 0x12. NodeJS Basics

## Description:bulb:

Getting started with Node JS

- Run JavaScript using NodeJS
- Use NodeJS modules
- Use specific NodeJS module to read files
- Use `process` to access command line arguments and the environment
- Create a small HTTP server using NodeJS
- Create a small HTTP server using ExpressJS
- Create advanced routes with ExpressJS
- Use ES6 with NodeJS with Babel-node
- Use Nodemon to develop faster

## Technologies & Tools:computer:

[![Jest](https://img.shields.io/badge/≡-Jest-C21325?logo=Jest&style=flat-square&labelColor=282828&logoColor=C21325)](https://jestjs.io/)
[![Git](https://img.shields.io/badge/≡-Git-F05032?logo=git&style=flat-square&labelColor=282828)](https://git-scm.com/)
[![Ubuntu](https://img.shields.io/badge/≡-Ubuntu-E95420?&style=flat-square&logo=Ubuntu&labelColor=282828)](https://ubuntu.com/)
[![Mocha](https://img.shields.io/badge/≡-Mocha-8D6748?logo=Mocha&style=flat-square&labelColor=282828)](https://mochajs.org/)
[![Babel](https://img.shields.io/badge/≡-Babel-F9DC3E?logo=Babel&style=flat-square&labelColor=282828)](https://babeljs.io/)
[![JavaScript](https://img.shields.io/badge/≡-JavaScript-F7DF1E?logo=javascript&style=flat-square&labelColor=282828)](https://developer.mozilla.org/en-US/docs/Web/javascript)
[![Nodemon](https://img.shields.io/badge/≡-Nodemon-76D04B?logo=Nodemon&style=flat-square&labelColor=282828)](https://github.com/remy/nodemon#nodemon)
[![GNU_Bash](https://img.shields.io/badge/≡-GNU_Bash-4EAA25?logo=GNU-Bash&style=flat-square&labelColor=282828)](https://www.gnu.org/software/bash/)
[![Nodejs](https://img.shields.io/badge/≡-Nodejs-339933?logo=Node.js&style=flat-square&labelColor=282828)](https://nodejs.org/en/)
[![Vim](https://img.shields.io/badge/≡-Vim-019733?logo=Vim&style=flat-square&logoColor=019733&labelColor=282828)](https://www.vim.org/)
[![Vagrant](https://img.shields.io/badge/≡-Vagrant-1563FF?logo=vagrant&style=flat-square&logoColor=1563FF&labelColor=282828)](https://www.vagrantup.com/)
[![VS_Code](https://img.shields.io/badge/≡-VS_Code-007ACC?logo=visual-studio-code&style=flat-square&logoColor=007ACC&labelColor=282828)](https://code.visualstudio.com/)
[![ESLint](https://img.shields.io/badge/≡-ESLint-4B32C3?logo=ESLint&style=flat-square&labelColor=282828&logoColor=4B32C3)](https://eslint.org/)
[![GitHub](https://img.shields.io/badge/≡-GitHub-181717?logo=GitHub&style=flat-square&labelColor=282828)](https://github.com/)
[![Express](https://img.shields.io/badge/≡-Express-000000?logo=Express&style=flat-square&labelColor=282828)](https://expressjs.com/)

---

## Resources:books:

Read or watch:

- [Node JS getting started](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Process API doc](https://node.readthedocs.io/en/latest/api/process/)
- [Child process](https://nodejs.org/api/child_process.html)
- [Express getting started](https://expressjs.com/en/starter/installing.html)
- [Mocha documentation](https://mochajs.org/)
- [Nodemon documentation](https://github.com/remy/nodemon#nodemon)

---

## Requirements:hammer:

- Ubuntu 18.04 LTS using NodeJS 12.xx.x
- Jest Testing Framework
- ESLint

### Install NodeJS 12.22.x

```console
foo@pop-os:~$ curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
foo@pop-os:~$ sudo bash nodesource_setup.sh
foo@pop-os:~$ sudo apt install nodejs -y
```

### Check version

```console
foo@pop-os:~$ nodejs -v
v12.22.1
foo@pop-os:~$ npm -v
6.14.12
```

### Install Jest, Babel, and ESLint

```console
foo@pop-os:~$ npm install --save-dev jest
foo@pop-os:~$ npm install --save-dev babel-jest @babel/core @babel/preset-env
foo@pop-os:~$ npm install --save-dev eslint
foo@pop-os:~$ npm install
```

---

## Files:card_file_box:

### [0. Executing basic javascript with Node JS](./0-console.js)

### [1. Using Process stdin](./1-stdin.js)

### [2. Reading a file synchronously with Node JS](./2-read_file.js)

### [3. Reading a file asynchronously with Node JS](./3-read_file_async.js)

### [4. Create a small HTTP server using Node's HTTP module](./4-http.js)

### [5. Create a more complex HTTP server using Node's HTTP module](./5-http.js)

### [6. Create a small HTTP server using Express](./6-http_express.js)

### [7. Create a more complex HTTP server using Express](./7-http_express.js)

### [8. Organize a complex HTTP server using Express](./full_server/utils.js)

---

## Author

- **Diego Monroy** (@diegozencode) - [<img src="https://img.shields.io/badge/Portfolio-20d6fe.svg?&style=plastic"/>](https://diegozencode.me)
  [<img src="https://img.shields.io/badge/Twitter-1DA1F2.svg?&style=plastic&logo=twitter&logoColor=white"/>](https://twitter.com/diegozencode)
  [<img src="https://img.shields.io/badge/Linkedin-0A66C2.svg?&style=plastic&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/diegozencode)
  [<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=plastic&logo=github&logoColor=white"/>](https://github.com/diegozencode)
