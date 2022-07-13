const AWS = require("aws-sdk");
const crypto = require("crypto");

// Generate unique id with no external dependencies
const generateUUID = () => crypto.randomBytes(16).toString("hex");

// Initialising the DynamoDB SDK
const documentClient = new AWS.DynamoDB.DocumentClient();

exports.handler = async event => {
  const { transactionId } = JSON.parse(event.body);
  const { transactionDate } = JSON.parse(event.body);
  const { transactionAmount } = JSON.parse(event.body);
  const { transactionBy } = JSON.parse(event.body);
  const { transactionStatus } = JSON.parse(event.body);
  
  const params = {
    TableName: "dth_transactions", // The name of your DynamoDB table
    Item: { // Creating an Item with a unique id and with the passed title
      transactionId: generateUUID(),
      transactionDate: transactionDate,
      transactionAmount: transactionAmount,
      transactionBy: transactionBy,
      transactionStatus: transactionStatus
    }
  };
  try {
    const data = await documentClient.put(params).promise();
    const response = {
      statusCode: 200
    };
    return response; // Returning a 200 if the item has been inserted 
  } catch (e) {
    return {
      statusCode: 500,
      body: JSON.stringify(e)
    };
  }
};
