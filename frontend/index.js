const http = require('http');

const PORT = 3000;
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end('<h1>Frontend funcionando correctamente en Docker!</h1>');
});

server.listen(PORT, () => {
  console.log(`Frontend corriendo en el puerto ${PORT}`);
});