import kue from 'kue';
const queue = kue.createQueue();

const job = queue.create('push_notification_code', { phoneNumber: '123-456-789', message: 'hello world' })
.save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`)
})
.on('complete', () => console.log('Notification job completed'))
.on('failed', () => console.log('Notification job completed'));
