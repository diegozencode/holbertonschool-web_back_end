// File System Module
const fs = require('fs');

const countStudents = (path) => {
  try {
    // Read file
    const data = fs.readFileSync(path, 'utf8').split('\n');
    const columns = data.slice(1, data.length);
    let counter = 0;
    const fields = {};
    for (const i of columns) {
      if (i) {
        counter += 1;
      }
      const row = i.split(',');
      if (!fields[row[3]] && row[3]) {
        fields[row[3]] = [];
      }
      if (row[0]) {
        fields[row[3]].push(row[0]);
      }
    }
    console.log(`Number of students: ${counter}`);
    for (const [key, value] of Object.entries(fields)) {
      if (key) {
        console.log(`Number of students in ${value.length}. List: ${value.join(', ')}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
