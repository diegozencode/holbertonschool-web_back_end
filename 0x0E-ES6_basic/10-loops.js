export default function appendToEachArrayValue(array, appendString) {
  for (const [key, value] of array) {
    array[key] = `${appendString}${value}`
  }

  return array;
}
