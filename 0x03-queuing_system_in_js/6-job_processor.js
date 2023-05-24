import kue from 'kue';
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};
const data = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', data)
.save((err) => {
  if (!err) sendNotification(data.phoneNumber, data.message)
});
