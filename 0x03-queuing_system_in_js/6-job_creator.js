#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queuee = createQueue({name: 'push_notification_code'});

const job_to_create = queuee.create('push_notification_code', {

  phoneNumber: '08117033382',
  message: 'Account just registered',

});

job_to_create
  .on('enqueue', () => {

    console.log('Notification job_to_create created:', job_to_create.id);

  })
  .on('complete', () => {

    console.log('Notification job_to_create completed');

  })
  .on('failed attempt', () => {

    console.log('Notification job_to_create failed');

  });
job_to_create.save();
