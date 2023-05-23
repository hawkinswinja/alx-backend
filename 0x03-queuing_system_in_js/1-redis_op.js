import redis from 'redis';
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (e) => {
    console.log(`Redis client not connected to the server: ${e}`);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => console.log(reply));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
