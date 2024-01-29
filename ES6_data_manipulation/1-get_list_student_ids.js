export default function getListStudentIds(studentsData) {
  if (Array.isArray(studentsData) == false) {
    return [];
  }
  const studentId = studentsData.map((arrayElement) => arrayElement.id);
  return studentId;
}
