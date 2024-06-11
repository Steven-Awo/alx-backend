import redis from 'redis';

const subscriberstoChannel = redis.createClient();

subscriberstoChannel.on('connect', function() {

  console.log('Redis client connected to the server');

});

subscriberstoChannel.on('error', function(err) {

  console.log('Redis client not connected to the server: ' + err);

});

subscriberstoChannel.subscribe('holberton school channel');

subscriberstoChannel.on('message', function(channel, message) {

  console.log(message);

  if (message === 'KILL_SERVER') {

    subscriberstoChannel.unsubscribe();

    subscriberstoChannel.quit();

  }
});
