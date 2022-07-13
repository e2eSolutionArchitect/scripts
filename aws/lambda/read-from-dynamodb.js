
const AWS = require('aws-sdk'); 

const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'}); 

exports.handler = async (event, context, callback) => {
    await readMessage().then(data => {
        data.Items.forEach(function(item) {
            console.log(item.message)
        });
        callback(null, {
            // If success return 200, and items
            statusCode: 200,
            body: data.Items,
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
        })
    }).catch((err) => {
        // If an error occurs write to the console
        console.error(err);
    })
};

function readMessage() {
    const params = {
        TableName: 'dth_transactions',
        Limit: 10
    }
    return ddb.scan(params).promise();
}
