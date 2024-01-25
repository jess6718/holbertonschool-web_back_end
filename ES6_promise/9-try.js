export default function guardrail(mathFunction) {
  const queue = [];
  const message = 'Guardrail was processed';
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(`Error: ${err.message}`);
  }
  queue.push(message);
  return queue;
}
