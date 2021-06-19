# 0x13. Unittests in JS

## Description:bulb:

You can't fail tests if you skip them

- How to use Mocha to write a test suite
- Ho0w to use different assertion libraries (Node or Chai)
- How to present long test suites
- When and how to use spies
- When and how to use stubs
- What are hooks and when to use them
- Unit testing with Async functions
- How to write integration tests with a small node server

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

- [Mocha documentation](https://mochajs.org/)
- [Chai](https://www.chaijs.com/api/)
- [Sinon](https://sinonjs.org/releases/v7.5.0/)
- [Express](https://expressjs.com/en/guide/routing.html)
- [Request](https://www.npmjs.com/package/request)
- [How to Test NodeJS Apps using Mocha, Chai and SinonJS](https://scotch.io/tutorials/how-to-test-nodejs-apps-using-mocha-chai-and-sinonjs)

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
foo@pop-os:~$ npm install --save-dev eslint
foo@pop-os:~$ npm install --save-dev mocha
foo@pop-os:~$ npm install
```

---

## Files:card_file_box:

### [0. Basic test with Mocha and Node assertion library](./package.json)

### [1. Combining descriptions](./1-calcul.js)

### [2. Basic test using Chai assertion library](./2-calcul_chai.js)

### [3. Spies](./utils.js)

### [4. Stubs](./4-payment.js)

### [5. Hooks](./5-payment.js)

### [6. Async tests with done](./6-payment_token.js)

### [7. Skip](./7-skip.test.js)

### [8. Basic Integration testing](./8-api/package.json)

### [9. Regex integration testing](./9-api/api.js)

### [10. Deep equality & Post integration testing](./10-api/api.js)

---

## Author

- **Diego Monroy** (@diegozencode) - [<img src="https://img.shields.io/badge/Portfolio-20d6fe.svg?&style=plastic"/>](https://diegozencode.me)
  [<img src="https://img.shields.io/badge/Twitter-1DA1F2.svg?&style=plastic&logo=twitter&logoColor=white"/>](https://twitter.com/diegozencode)
  [<img src="https://img.shields.io/badge/Linkedin-0A66C2.svg?&style=plastic&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/diegozencode)
  [<img src="https://img.shields.io/badge/GitHub-181717.svg?&style=plastic&logo=github&logoColor=white"/>](https://github.com/diegozencode)
