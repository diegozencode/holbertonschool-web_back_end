export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;

  return students.reduce(reducer, 0);
}
