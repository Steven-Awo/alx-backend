import { createClient, print } from 'redis';

const clientt = createClient();

clientt.on('error', (err) => {

  console.log('Redis client not connected to the server:', err.message);

});

clientt.on('connect', () => {

  console.log('Redis client connected to the server');

});

clientt.connect().catch((err) => {

  console.log('Redis client not connected to the server:', err.message);

});

function setNewSchool(schoolName, value) {

  clientt.set(schoolName, value, print);

}

function displaySchoolValue(schoolName) {

  clientt.get(schoolName, (err, reply) => {
    if (err) {

      console.error(`Error when fetching the value for ${schoolName}: ${err.message}`);

      return;
    }

    console.log(reply);

  });
}

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValue('HolbertonSanFrancisco');
