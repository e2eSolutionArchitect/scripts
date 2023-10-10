const {SQS, SendMessageCommand,ReceiveMessageCommand,DeleteMessageCommand} = require("@aws-sdk/client-sqs");
require('dotenv').config();
const { v4: uuidv4 } = require('uuid');

const s3file = require("./download");
const msgProducer = require("./producer");
var fileName = "test-doc1.pdf"; 

const sqsClient = new SQS({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY,
        secretAccessKey: process.env.AWS_ACCESS_SECRET_KEY
    }
});


const fileId = generateUniqueId();
function generateUniqueId() {
    return uuidv4();
  };

var messageAttributes = {
    "FileId": {DataType: "String", StringValue: fileId},
    "FileKey": {DataType: "String", StringValue: "uploads/"},
    "FileName": {DataType: "String", StringValue: fileName}
};



msgProducer.SendMessageToQueue("new File scan request",messageAttributes);

const PullMessagesFromQueue = async () => {
    try{
        const command = new ReceiveMessageCommand({
            AttributeNames: [
                "SentTimestamp"
             ],
             MaxNumberOfMessages: 10,
            QueueUrl: process.env.AWS_SQS_QUEUE_URL_AWAITING,
            WaitTimeSeconds: 5,
            MessageAttributeNames: [
                "All"
             ],
            VisibilityTimeout: 10,

        });
        const result = await sqsClient.send(command);
        // console.log(result.Messages);

        // do some message processing 
        ProcessMessage(result);
    } catch (error) {
        console.log(error);
    }
};

PullMessagesFromQueue();

const DeleteMessageFromQueue = async (ReceiptHandle) => {
    var resp =false;
    try{
        const data = await sqsClient.send(new DeleteMessageCommand({
            QueueUrl: process.env.AWS_SQS_QUEUE_URL_AWAITING,
            ReceiptHandle: ReceiptHandle,
        }))
        resp =true;
        console.log("deleted successfully......");
    } catch (error) {
        console.log(error);
    }
    return resp;
};


const ProcessMessage = async (result) => {
    try{
        // read the message attributes and pull the file from s3 bucket
        console.log('calling ProcessMessage');
        console.log(result.Messages);

        var msgAttrs = result.Messages[0].MessageAttributes;
        var download_result = await s3file.download(msgAttrs.FileKey.StringValue+msgAttrs.FileName.StringValue);
        if(download_result){
            // post processing delete the current message and recreate a copy with status:scanned attribute to SCANNED queue
            // delete the message after successful processing
            const del_result = await DeleteMessageFromQueue(result.Messages[0].ReceiptHandle);
            console.log(del_result);
        }

    } catch (error) {
        console.log(error);
    }
};