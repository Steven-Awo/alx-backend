import { createClient } from 'redis';

async function main() {

  const client = createClient();

  client.on('connect', function() {

    console.log('Redis client connected to the server');

  });

  client.on('error', function(err) {

    console.log('Redis client not connected to the server:', err.message);

  });

  try {

    await client.connect();

  } catch (err) {

    console.log('Redis client not connected to the server:', err.message);

  }
}

main();
