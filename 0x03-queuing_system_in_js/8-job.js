#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

/**
 * Created the push notification for jobs thats
 * from the given  array of the jobs information.
 * @param {Job[]} jobs
 * @param {Queue} queue
 */

export const createPushNotificationsJobs = (jobs, queue) => {

  if (!(jobs instanceof Array)) {

    throw new Error('Jobs is not an array');

}
  for (const the_job_Informa of jobs) {

    const work = queue.create('push_notification_code_3', the_job_Informa);

    work
      .on('enqueue', () => {

        console.log('Notification job created:', work.id);

      })

      .on('complete', () => {

        console.log('Notification job', work.id, 'completed');

      })

      .on('failed', (err) => {

        console.log('Notification job', work.id, 'failed:', err.message || err.toString());

      })

      .on('progress', (progress, _data) => {

        console.log('Notification job', work.id, `${progress}% complete`);

      });

    work.save();

  }
};

export default createPushNotificationsJobs;
