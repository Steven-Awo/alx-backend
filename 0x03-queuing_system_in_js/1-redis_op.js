import redis from 'redis';

const clientt = redis.createClient();

clientt.on('connect', () => {

  console.log('Redis client connected to the server');

});

clientt.on('error', (err) => {

  console.error(`Redis client not connected to the server: ${err}`);

});

function setNewSchool(schoolName, value) {

  clientt.set(schoolName, value, redis.print);

}

function displaySchoolValue(schoolName) {

  clientt.get(schoolName, (err, reply) => {
    console.log(reply);

  });
}

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValue('HolbertonSanFrancisco');
