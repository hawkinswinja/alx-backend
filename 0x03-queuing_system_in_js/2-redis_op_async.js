import redis from 'redis';
import { promisify } from 'util';
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

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const val = await get(schoolName);
  console.log(val);
};

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
