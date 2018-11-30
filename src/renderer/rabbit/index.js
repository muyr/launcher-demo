var amqp = require('amqplib/callback_api')
var rabbitChannel
var requestQueue = 'electron.nuke'

amqp.connect('amqp://localhost', function (err, conn) {
  if (err) {
    console.log(err)
  } else {
    conn.createChannel(function (err, ch) {
      if (err) {
        console.log(err)
      } else {
        ch.assertQueue(requestQueue, {durable: false})
        rabbitChannel = ch
      }
    })
  }
})

function guid () {
  function S4 () {
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1)
  }

  return (S4() + S4() + '-' + S4() + '-' + S4() + '-' + S4() + '-' + S4() + S4() + S4())
}

export {rabbitChannel, requestQueue, guid}
