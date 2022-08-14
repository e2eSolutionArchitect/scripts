// return format has been changed with custom id "contracts" instead of "Items". To understand the diff pelase compare v2 and v3

const AWS = require("aws-sdk");
const crypto = require("crypto");
const dynamo = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'}); 

// Generate unique id with no external dependencies
const generateUUID = () => crypto.randomBytes(16).toString("hex");
const db_tableName = "dih_contracts"


exports.handler = async (event, context) => {
  let cid =generateUUID()
  let body;
  let statusCode = 200;

// Use event.pathParameters.id if passing param like /items/{id} in url
// event.queryStringParameters.id (query parameter) if passing param as query parameter like /items?id={id}
// query param must be configured in api gateway under 'request method'
  
  try {
    switch (event.httpMethod) {
      case "DELETE": //"DELETE /items/{id}":
            const params = {
                TableName: db_tableName,
                Key: {
                  id: event.queryStringParameters.id 
                }
            }
        await dynamo
          .delete(params).promise();
        //body = `Deleted contract ${event.queryStringParameters.id}`;
        body = JSON.stringify({"id":event.queryStringParameters.id});
        break;
      case "GET": //"GET /items":
        if (event.pathParameters != null) {
            body = await dynamo
              .get({
                TableName: db_tableName,
                Key: {
                  id: event.pathParameters.id
                }
              })
              .promise();
              //body = JSON.stringify(body);
            body = JSON.stringify({"contracts":body.Item});  
        } else {
            const params = {
                TableName: db_tableName,
                Limit: 10
            }
            body = await dynamo.scan(params).promise();
            //body=body.Items
            body = JSON.stringify({"contracts":body.Items});
        }
            //body = JSON.stringify(body.Items);
        break;
      case "POST":
        let requestJSON = JSON.parse(event.body);
        const postParams = {
            TableName: db_tableName,
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
        body = JSON.stringify(body);
        break;
      case "PUT":
        let requestUpdateJSON = JSON.parse(event.body);
        await dynamo
          .put({
            TableName: db_tableName,
            Item: {
              id: event.pathParameters.id,
              productId: requestUpdateJSON.productId,
              category: requestUpdateJSON.category,
              name: requestUpdateJSON.name,
              description: requestUpdateJSON.description,
              tags: requestUpdateJSON.tags,
              sku: requestUpdateJSON.sku,
              barcode: requestUpdateJSON.barcode,
              brand: requestUpdateJSON.brand,
              vendor: requestUpdateJSON.vendor,
              stock: requestUpdateJSON.stock,
              reserved: requestUpdateJSON.reserved,
              cost: requestUpdateJSON.cost,
              basePrice: requestUpdateJSON.basePrice,
              taxPercent: requestUpdateJSON.taxPercent,
              price: requestUpdateJSON.price,
              weight: requestUpdateJSON.weight,
              thumbnail: requestUpdateJSON.thumbnail,
              images: requestUpdateJSON.images,
              active: requestUpdateJSON.active
            }
          })
          .promise();
        body = `Put item ${event.pathParameters.id}`;
        body = JSON.stringify(body);
        break;
      default:
        throw new Error(`Unsupported route: "${event.httpMethod}"`);
    }
  } catch (err) {
    statusCode = 400;
    body = err.message;
  } 
  
  return {
    statusCode: statusCode,
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin" : "*"
    },
    //body: JSON.stringify({"contracts":body}) // set1
    body:body 
};
};

