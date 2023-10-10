const {SQS, SendMessageCommand} = require("@aws-sdk/client-sqs");
require('dotenv').config();
const sqsClient = new SQS({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY,
        secretAccessKey: process.env.AWS_ACCESS_SECRET_KEY
    }
});

const SendMessageToQueue = async (body,messageAttributes) => {
    try{
        const command = new SendMessageCommand({
            MessageBody: body,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL_AWAITING,
            MessageAttributes: messageAttributes,
        });
        const result = await sqsClient.send(command);
        console.log(result);
    } catch (error) {
        console.log(error);
    }
};

//SendMessageToQueue("File scan request");

module.exports = { SendMessageToQueue };