import fs from 'fs';

const readDatabase = async (path) => {
  try {
    // Read file
    const data = await fs.promises.readFile(path, 'utf8');
    const columns = data.split('\n').slice(1, data.length);
    const fields = {};
    for (const i of columns) {
      const row = i.split(',');
      if (!fields[row[3]] && row[3]) {
        fields[row[3]] = [];
      }
      if (row[0]) {
        fields[row[3]].push(row[0]);
      }
    }
    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

export default readDatabase;
