import redis from 'redis';

const clientt = redis.createClient();

clientt.hset("HolbertonSchools", "Portland", 50, redis.print);

clientt.hset("HolbertonSchools", "Seattle", 80, redis.print);

clientt.hset("HolbertonSchools", "New York", 20, redis.print);

clientt.hset("HolbertonSchools", "Bogota", 20, redis.print);

clientt.hset("HolbertonSchools", "Cali", 40, redis.print);

clientt.hset("HolbertonSchools", "Paris", 2, redis.print);

clientt.hgetall("HolbertonSchools", function(err, reply) {

  console.log(reply);

});
