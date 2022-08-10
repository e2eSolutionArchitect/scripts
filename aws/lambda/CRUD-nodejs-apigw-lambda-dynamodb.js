// This code is to create a single lambda function for GET, DELETE, POST and integrate with a single apigw. 
// in APIGW make sure your create resources like below
```
- contract
--GET
--POST
----contract/{id} // {id} this resource is under parent 'contract' resource where resource path is simply {id}
-----DELETE
-----GET
```
// Below is the lambda code in NodeJS. add it in index.js 

const AWS = require("aws-sdk");
const crypto = require("crypto");
const dynamo = new AWS.DynamoDB.DocumentClient();

// Generate unique id with no external dependencies
const generateUUID = () => crypto.randomBytes(16).toString("hex");

exports.handler = async (event, context) => {
  let cid =generateUUID()
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };

  try {
    switch (event.httpMethod) {
      case "DELETE":
            const params = {
                TableName: 'dih_contracts',
                Key: {
                  id: event.pathParameters.id
                }
            }
        await dynamo
          .delete(params).promise();
        body = `Deleted contract ${event.pathParameters.id}`;
        break;
      case "GET":
        if (event.pathParameters != null) {
            body = await dynamo
              .get({
                TableName: "dih_contracts",
                Key: {
                  id: event.pathParameters.id
                }
              })
              .promise();
        } else {
            const params = {
                TableName: 'dih_contracts',
                Limit: 10
            }
            body = await dynamo.scan(params).promise();
        }
        break;
      case "POST":
        let requestJSON = JSON.parse(event.body);
        const postParams = {
            TableName: "dih_contracts",
            Item: {
                  id: cid,
                  productId: requestJSON.productId,
                  category: requestJSON.category,
                  name: requestJSON.name,
                  description: requestJSON.description,
                  tags: requestJSON.tags,
                  sku: requestJSON.sku,
                  barcode: requestJSON.barcode,
                  brand: requestJSON.brand,
                  vendor: requestJSON.vendor,
                  stock: requestJSON.stock,
                  reserved: requestJSON.reserved,
                  cost: requestJSON.cost,
                  basePrice: requestJSON.basePrice,
                  taxPercent: requestJSON.taxPercent,
                  price: requestJSON.price,
                  weight: requestJSON.weight,
                  thumbnail: requestJSON.thumbnail,
                  images: requestJSON.images,
                  active: requestJSON.active
            }
          }
        await dynamo.put(postParams).promise();
        body = `Added/Updated contract ${cid}`;
        break;
      default:
        throw new Error(`Unsupported route: "${event.httpMethod}"`);
    }
  } catch (err) {
    statusCode = 400;
    body = err.message;
  } finally {
    body = JSON.stringify(body);
  }

  return {
    statusCode,
    body,
    headers
  };
};
