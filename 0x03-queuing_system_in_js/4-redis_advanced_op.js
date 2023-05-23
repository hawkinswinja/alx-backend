import redis from 'redis';
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (e) => {
    console.log(`Redis client not connected to the server: ${e}`);
  });

const data = { 
  Portland: 50,
  Seattle: 80,
	"New York": 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2
};

for (const [k, v] of Object.entries(data)) {
  client.hset('HolbertonSchools', k, v, redis.print);
}

client.hgetall('HolbertonSchools', (err, reply) => console.log(reply));
