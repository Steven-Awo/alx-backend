#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

const The_Blacklisted_Numbs = ['4153518780', '4153518781'];

const queuees = createQueue();

/**
 * Sends just a push of a notification to the user.
 * @param {String} phoneNumber
 * @param {String} message
 * @param {Job} job
 * @param {*} done
 */

const sendNotification = (phoneNumber, message, job, done) => {

  let totally = 2;

  let pendding = 2;

  let send_interval = setInterval(() => {

    if (totally - pendding <= totally / 2) {

      job.progress(totally - pendding, totally);

    }

    if (The_Blacklisted_Numbs.includes(phoneNumber)) {

      done(new Error(`Phone number ${phoneNumber} is blacklisted`));

      clearInterval(send_interval);

      return;

    }

    if (totally === pendding) {

      console.log(

        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );

    }

    --pendding || done();

    pendding || clearInterval(send_interval);

  }, 1000);
};

queuees.process('push_notification_code_2', 2, (job, done) => {

  sendNotification(
    job.data.phoneNumber, job.data.message, job, done);
});
