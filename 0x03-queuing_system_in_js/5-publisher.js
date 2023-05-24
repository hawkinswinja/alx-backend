import redis from 'redis';
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (e) => {
    console.log(`Redis client not connected to the server: ${e}`);
  });

function sleep(t) {
  return new Promise((r) => setTimeout(r, t));
};

async function publishMessage(message, time) {
  await sleep(time);
  console.log(`About to send ${message}`);
	client.publish('holberton school channel', message);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
