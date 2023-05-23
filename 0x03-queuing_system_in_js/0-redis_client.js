import { createClient } from 'redis';
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (e) => {
  console.log(`Redis client not connected to the server: ${e}`);
});

process.on('SIGINT', () => {
  client.quit();
  process.exit();
});
