#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queuees = createQueue();

const sendNotification = (phoneNumber, message) => {

  console.log(

    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );

};

queuees.process('push_notification_code', (job, done) => {

  sendNotification(job.data.phoneNumber, job.data.message);

  done();

});
