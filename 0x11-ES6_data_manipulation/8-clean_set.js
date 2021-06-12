export default function cleanSet(set, startString) {
  let result = '';
  if (startString && typeof startString === 'string') {
    set.forEach((i) => {
      if (i.startsWith(startString)) {
        result += `${i.slice(startString.length)}-`;
      }
    });
    return result.slice(0, result.length - 1);
  }
  return result;
}
