import redis from 'redis';
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (e) => {
    console.log(`Redis client not connected to the server: ${e}`);
  })
	.on('message', (channel, message) => { 
    console.log(message);
    if (message === 'KILL_SERVER')
      client.unsubscribe();
  })
  .subscribe('holberton school channel', (message, channel) => {});
