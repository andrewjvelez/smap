module.exports = async function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.pid) {
        const pid = req.query.pid;
        var send = require('gmail-send')({
            //var send = require('../index.js')({
            user: 'raspberrypi.schroders@gmail.com',
            // user: credentials.user,                  // Your GMail account used to send emails
            pass: 'Schroders1/',
            // pass: credentials.pass,                  // Application-specific password
            to: 'draperj.ct@gmail.com',
            // to:   credentials.user,                  // Send to yourself
            // you also may set array of recipients:
            // [ 'user1@gmail.com', 'user2@gmail.com' ]
            // from:    credentials.user,            // from: by default equals to user
            // replyTo: credentials.user,            // replyTo: by default undefined
            // bcc: 'some-user@mail.com',            // almost any option of `nodemailer` will be passed to it
            subject: 'PiMail test',
            // text: 'gmail-send example 1',         // Plain text
            html: '<b>Hello Pi azure functions world for ' + pid + '!!👌💯🎉</b>'            // HTML
        });


        send({}, function (err, res) {
            consolge.log(Date.now(), '* \send() callback returned: err: ', err, ', res: ', res);
        });

        context.res = {
            // status: 200, /* Defaults to 200 */
            body: "Email message sent for pid " + pid
        };
    }
    else {
        context.res = {
            status: 400,
            body: "Please pass an query string parameter 'pid' to the function"
        };
    }
};