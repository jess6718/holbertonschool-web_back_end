export default function getStudentsByLocation(studentsData, city) {
  const array = studentsData.filter((arrayElement) => arrayElement.location === city);
  return array;
}
