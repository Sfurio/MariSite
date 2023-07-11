const canvas = document.getElementById('signature-canvas');
const clearButton = document.getElementById('clear-button');
const signatureDataInput = document.getElementById('signature-data');
const context = canvas.getContext('2d');
let isDrawing = false;

function startDrawing(event) {
  isDrawing = true;
  const { offsetX, offsetY } = event;
  context.beginPath();
  context.moveTo(offsetX, offsetY);
}

function draw(event) {
  if (!isDrawing) return;
  const { offsetX, offsetY } = event;
  context.lineTo(offsetX, offsetY);
  context.stroke();
}

function stopDrawing() {
  isDrawing = false;
  const imageData = canvas.toDataURL();
  signatureDataInput.value = imageData;
}

function clearCanvas() {
  context.clearRect(0, 0, canvas.width, canvas.height);
  signatureDataInput.value = '';
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);
clearButton.addEventListener('click', clearCanvas);
