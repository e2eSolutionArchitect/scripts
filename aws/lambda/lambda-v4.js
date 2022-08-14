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


  try {
    switch (event.httpMethod) {
      case "DELETE": //"DELETE /items/{id}":
            const params = {
                TableName: db_tableName,
                Key: {
                  id: event.queryStringParameters.id //event.pathParameters.id
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
        //body = `Added/Updated contract ${cid}`;
        body = JSON.stringify(postParams.Item);
        break;
      case "PUT":
        let requestUpdateJSON = JSON.parse(event.body);
        const updateParams = {
            TableName: db_tableName,
            Item: {
                  id: requestUpdateJSON.contract.id, //event.pathParameters.id, requestUpdateJSON.id
                  productId: requestUpdateJSON.contract.productId,
                  category: requestUpdateJSON.contract.category,
                  name: requestUpdateJSON.contract.name,
                  description: requestUpdateJSON.contract.description,
                  tags: requestUpdateJSON.contract.tags,
                  sku: requestUpdateJSON.contract.sku,
                  barcode: requestUpdateJSON.contract.barcode,
                  brand: requestUpdateJSON.contract.brand,
                  vendor: requestUpdateJSON.contract.vendor,
                  stock: requestUpdateJSON.contract.stock,
                  reserved: requestUpdateJSON.contract.reserved,
                  cost: requestUpdateJSON.contract.cost,
                  basePrice: requestUpdateJSON.contract.basePrice,
                  taxPercent: requestUpdateJSON.contract.taxPercent,
                  price: requestUpdateJSON.contract.price,
                  weight: requestUpdateJSON.contract.weight,
                  thumbnail: requestUpdateJSON.contract.thumbnail,
                  images: requestUpdateJSON.contract.images,
                  active: requestUpdateJSON.contract.active
            }
          }
        await dynamo.put(updateParams).promise();
        //body = `Put item ${event.pathParameters.id}`;
        body = JSON.stringify(updateParams.Item);
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

