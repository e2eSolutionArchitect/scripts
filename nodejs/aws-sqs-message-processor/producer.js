const {SQS, SendMessageCommand,ReceiveMessageCommand} = require("@aws-sdk/client-sqs");
require('dotenv').config();

const sqsClient = new SQS({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY,
        secretAccessKey: process.env.AWS_ACCESS_SECRET_KEY
    }
});

const { v4: uuidv4 } = require('uuid');

function generateUniqueId() {
  return uuidv4();
}

// Usage example
const fileId = generateUniqueId();
console.log('Generated Message ID:', fileId);


const sendMessageToQueue = async (body) => {
    try{
        const command = new SendMessageCommand({
            MessageBody: body,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL,
            MessageAttributes:{
                FileId: {DataType: "String", StringValue: fileId},
                FileName: {DataType: "String", StringValue: "test.png"},
            },
        });
        const result = await sqsClient.send(command);
        console.log(result);
    } catch (error) {
        console.log(error);
    }
};

//sendMessageToQueue("My first message to the world")

const pullMessagesFromQueue = async () => {
    try{
        const command = new ReceiveMessageCommand({
            MaxNumberOfMessages: 10,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL,
            WaitTimeSeconds: 5,
            MessageAttributes: ["All"],
            VisibilityTimeout: 10,

        });
        const result = await sqsClient.send(command);
        console.log(result);
    } catch (error) {
        console.log(error);
    }
};
pullMessagesFromQueue()