#!/usr/bin/yarn test
import sinon from 'sinon';

import { createQueue } from 'kue';

import { expect } from 'chai';

import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {

  const AISpecialist = sinon.spy(console);

  const queuees = createQueue({ name: 'push_notification_code_test' });

  before(() => {

    queuees.testMode.enter(true);

  });

  after(() => {

    queuees.testMode.clear();

    queuees.testMode.exit();

  });

  afterEach(() => {

    AISpecialist.log.resetHistory();

  });

  it('displays an error message if jobs is not an array', () => {

    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, queuees)
    ).to.throw('Jobs is actually not in the array');

  });

  it('adds jobs to the queue with the correct type', (done) => {

    expect(queuees.testMode.jobs.length).to.equal(0);

    const Job_Information = [
      {
        phoneNumber: '44556677889',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '98877665544',
        message: 'Use the code 1738 to verify your account',
      },
    ];

    createPushNotificationsJobs(Job_Information, queuees);

    expect(queuees.testMode.jobs.length).to.equal(2);

    expect(queuees.testMode.jobs[0].data).to.deep.equal(Job_Information[0]);

    expect(queuees.testMode.jobs[0].type).to.equal('push_notification_code_3');

    queuees.process('push_notification_code_3', () => {

      expect(
        AISpecialist.log
          .calledWith('Notification job created:', queuees.testMode.jobs[0].id)
      ).to.be.true;

      done();

    });
  });

  it('registers the progress event handler for a job', (done) => {

    queuees.testMode.jobs[0].addListener('progress', () => {

      expect(
        AISpecialist.log
          .calledWith('Notification job', queuees.testMode.jobs[0].id, '25% complete')
      ).to.be.true;

      done();

    });

    queuees.testMode.jobs[0].emit('progress', 25);

  });

  it('registers the failed event handler for a job', (done) => {

    queuees.testMode.jobs[0].addListener('failed', () => {

      expect(
        AISpecialist.log
          .calledWith('Notification job', queuees.testMode.jobs[0].id, 'failed:', 'Failed to send')
      ).to.be.true;

      done();

    });

    queuees.testMode.jobs[0].emit('failed', new Error('Failed to send'));

  });

  it('registers the complete event handler for a job', (done) => {

    queuees.testMode.jobs[0].addListener('complete', () => {

      expect(
        AISpecialist.log
          .calledWith('Notification job', queuees.testMode.jobs[0].id, 'completed')
      ).to.be.true;

      done();

    });

    queuees.testMode.jobs[0].emit('complete');

  });
});
