const {SQS,ReceiveMessageCommand,DeleteMessageCommand} = require("@aws-sdk/client-sqs");
require('dotenv').config();

const sqsClient = new SQS({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY,
        secretAccessKey: process.env.AWS_ACCESS_SECRET_KEY
    }
});


const PullMessagesFromQueue = async () => {
    try{
        const command = new ReceiveMessageCommand({
            MaxNumberOfMessages: 10,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL,
            WaitTimeSeconds: 5,
            MessageAttributes: ["All"],
            VisibilityTimeout: 10,

        });
        const result = await sqsClient.send(command);
        //console.log(result.Messages);

        // do some message processing 
        ProcessMessage(result);
        // delete the message after successful processing
        const del_result = await DeleteMessageFromQueue(result.Messages[0].ReceiptHandle);
    } catch (error) {
        console.log(error);
    }
};

PullMessagesFromQueue();

const DeleteMessageFromQueue = async (ReceiptHandle) => {
    try{
        const data = await sqsClient.send(new DeleteMessageCommand({
            QueueUrl: process.env.AWS_SQS_QUEUE_URL,
            ReceiptHandle: ReceiptHandle,
        }))
        console.log("deleted successfully......");
    } catch (error) {
        console.log(error);
    }
};



const ProcessMessage = async (result) => {
    try{
        console.log('calling ProcessMessage');
        console.log(result.Messages);
    } catch (error) {
        console.log(error);
    }
};