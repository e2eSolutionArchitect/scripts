const {SQS, SendMessageCommand,ReceiveMessageCommand,DeleteMessageCommand} = require("@aws-sdk/client-sqs");
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

const fileId = generateUniqueId();


const SendMessageToQueue = async (body) => {
    try{
        const command = new SendMessageCommand({
            MessageBody: body,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL_AWAITING,
            MessageAttributes:{
                FileId: {DataType: "String", StringValue: fileId},
                FileName: {DataType: "String", StringValue: "test.png"},
                FileS3URI: {DataType: "String", StringValue: "s3://e2esa-demo/uploads/fileup.pdf"},
            },
        });
        const result = await sqsClient.send(command);
        console.log(result);
    } catch (error) {
        console.log(error);
    }
};

SendMessageToQueue("File scan request for fileId: "+fileId)

const PullMessagesFromQueue = async () => {
    try{
        const command = new ReceiveMessageCommand({
            MaxNumberOfMessages: 10,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL_AWAITING,
            WaitTimeSeconds: 5,
            MessageAttributes: ["All"],
            VisibilityTimeout: 10,

        });
        const result = await sqsClient.send(command);
        //console.log(result.Messages);

        // do some message processing 
        ProcessMessage(result);
        // delete the message after successful processing
        //const del_result = await DeleteMessageFromQueue(result.Messages[0].ReceiptHandle);
    } catch (error) {
        console.log(error);
    }
};

PullMessagesFromQueue();

const DeleteMessageFromQueue = async (ReceiptHandle) => {
    try{
        const data = await sqsClient.send(new DeleteMessageCommand({
            QueueUrl: process.env.AWS_SQS_QUEUE_URL_AWAITING,
            ReceiptHandle: ReceiptHandle,
        }))
        console.log("deleted successfully......");
    } catch (error) {
        console.log(error);
    }
};



const ProcessMessage = async (result) => {
    try{
        // read the message attributes and pull the file from s3 bucket
        console.log('calling ProcessMessage');
        console.log(result.Messages);
        // post processing delete the current message and recreate a copy with status:scanned attribute to SCANNED queue
    } catch (error) {
        console.log(error);
    }
};
