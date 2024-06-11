import redis from 'redis';

import { promisify } from 'util';

const clientt = redis.createClient();

clientt.on('connect', () => {

  console.log('Redis client connected to the server');

});

clientt.on('error', (err) => {

  console.error(`Redis client not connected to the server: ${err}`);

});

function setNewSchool(schoolName, value) {

  return new Promise((resolve, reject) => {

    clientt.set(schoolName, value, (err, reply) => {

      if (err) reject(err);

      else {

        console.log('Reply: OK');

        resolve(reply);
      }
    });
  });
}

async function displaySchoolValue(schoolName) {

  const getting_Async = promisify(clientt.get).bind(clientt);

  const replyy = await getting_Async(schoolName);

  console.log(replyy);
}

async function main() {

  await displaySchoolValue('Holberton');

  await setNewSchool('HolbertonSanFrancisco', '100');

  await displaySchoolValue('HolbertonSanFrancisco');

}

main().catch(err => console.error(err));

