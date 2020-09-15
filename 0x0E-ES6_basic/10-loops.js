export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const [key, value] of newArray.entries()) {
    newArray[key] = `${appendString}${value}`;
  }

  return newArray;
}
