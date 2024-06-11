#!/usr/bin/yarn dev
import express from 'express';

import { createClient } from 'redis';

import { createQueue } from 'kue';

import { promisify } from 'util';

const app = express();

const client = createClient({ name: 'reserve_seat' });

const queue = createQueue();

const INITIAL_SEATS_COUNT = 50;

let reservationEnabled = false;

const PORT = 1245;

/**
 * Modifies all the number of the seats that are available.
 * @param {number} number - The new number of seats.
 */
const reserveSeat = async (number) => {

  return promisify(client.SET).bind(client)('available_seats', number);

};

/**
 * Retrieves all the number of the seats that are available.
 * @returns {Promise<String>}
 */

const getCurrentAvailableSeats = async () => {

  return promisify(client.GET).bind(client)('available_seats');

};

app.get('/available_seats', (_, res) => {

  getCurrentAvailableSeats()
    // .then(result => Number.parseInt(result || 0))
    .then((numberOfAvailableSeats) => {

      res.json({ numberOfAvailableSeats })
    });

});

app.get('/reserve_seat', (_req, res) => {

  if (!reservationEnabled) {

    res.json({ status: 'Reservation are blocked' });

    return;

  }
  try {

    const jobb = queue.create('reserve_seat');

    jobb.on('failed', (err) => {

      console.log('Seat reservation job',
        jobb.id,
        'failed:',
        err.message || err.toString(),
      );

    });

    jobb.on('complete', () => {

      console.log('Seat reservation job',
        jobb.id,
        'completed'
      );

    });

    jobb.save();

    res.json({ status: 'Reservation in process' });

  } catch {

    res.json({ status: 'Reservation failed' });

  }
});

app.get('/process', (_req, res) => {

  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', (_job, done) => {

    getCurrentAvailableSeats()
      .then((result) => Number.parseInt(result || 0))
      .then((availableSeats) => {

        reservationEnabled = availableSeats <= 1 ? false : reservationEnabled;

        if (availableSeats >= 1) {

          reserveSeat(availableSeats - 1)
            .then(() => done());

        } else {

          done(new Error('Not enough seats available'));

        }
      });
  });
});

const resetAvailableSeats = async (initialSeatsCount) => {

  return promisify(client.SET)
    .bind(client)('available_seats', Number.parseInt(initialSeatsCount));

};

app.listen(PORT, () => {

  resetAvailableSeats(process.env.INITIAL_SEATS_COUNT || INITIAL_SEATS_COUNT)
    .then(() => {

      reservationEnabled = true;

      console.log(`API available on localhost port ${PORT}`);

    });
});

export default app;
