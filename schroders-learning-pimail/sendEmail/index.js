const moment = require('moment');
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.piName) {
        const piName = req.query.piName;
        const date = moment(Date.now()).format('MMMM Do YYYY, h:mm:ss a')
        var send = require('gmail-send')({
            //var send = require('../index.js')({
            user: 'SmapAlert@gmail.com',
            // user: credentials.user,                  // Your GMail account used to send emails
            pass: 'Schroders1/',
            // pass: credentials.pass,                  // Application-specific password
            to: ['andrew.velez@schroders.com', 'draperj.ct@gmail.com'],
            // to:   credentials.user,                  // Send to yourself
            // you also may set array of recipients:
            // [ 'user1@gmail.com', 'user2@gmail.com' ]
            // from:    credentials.user,            // from: by default equals to user
            // replyTo: credentials.user,            // replyTo: by default undefined
            // bcc: 'some-user@mail.com',            // almost any option of `nodemailer` will be passed to it
            subject: 'An issue has been reported for ' + piName,
            // text: 'gmail-send example 1',         // Plain text
            html: '<h1><b>An issue has been reported for ' + piName + '</b></h1><p>A user has reported the issue at ' + date + '.</p><p>Please troubleshoot ' + piName + ' at your earliest convenience.</p>'            // HTML
        });


        return send({}, function (err, res) {
            let message = "";
            if (err) {
                context.log(Date.now(), '*ERROR* \send() callback returned: err: ', err, ', res: ', res);
                message = "Error sending email. Debug message - " + err;

                context.res = {
                    status: 400,
                    body: message
                };
            } else {
                context.log(Date.now(), '*SUCCESS* \send() callback returned: res: ', res);
                message = "Success sending email. Debug message - " + res;

                context.res = {
                    status: 200,
                    body: message
                };
            }

            context.done();
        });
    }
    else {
        context.res = {
            status: 400,
            body: "Please pass an query string parameter 'pid' to the function"
        };

        context.done();
    }
};