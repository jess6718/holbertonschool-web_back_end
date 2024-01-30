export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  // Create an ArrayBuffer of the specified length
  const buffer = new ArrayBuffer(length);
  // Create an Int8Array using the buffer
  const int8Array = new Int8Array(buffer);
  // Assign the value at the specified position
  int8Array[position] = value;
  // Return a DataView for the buffer
  return new DataView(buffer);
}
