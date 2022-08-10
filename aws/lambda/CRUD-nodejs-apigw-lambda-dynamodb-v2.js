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
const dynamo = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'}); 

// Generate unique id with no external dependencies
const generateUUID = () => crypto.randomBytes(16).toString("hex");
const db_tableName = "dih_contracts"

exports.handler = async (event, context) => {
  let cid =generateUUID()
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };

  try {
    switch (event.httpMethod) {
      case "DELETE": //"DELETE /items/{id}":
            const params = {
                TableName: db_tableName,
                Key: {
                  id: event.pathParameters.id
                }
            }
        await dynamo
          .delete(params).promise();
        body = `Deleted contract ${event.pathParameters.id}`;
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
        } else {
            const params = {
                TableName: db_tableName,
                Limit: 10
            }
            body = await dynamo.scan(params).promise();
        }
        break;
      case "GET /find":
        body = searchByBrand(event.pathParameters.param)
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

// custom function for Dynamic Search
async function searchByBrand(inp){
    try {
        var params = {
            Key: {
             "brand": inp
            }, 
            TableName: db_tableName
        };
        var result = await dynamo.query(params).promise()
        console.log(JSON.stringify(result))
    } catch (error) {
        console.error(error);
    }
}

// input for test
```
{
  "category": "20842e9d185cf66455586dd05b548a5f",
  "name": "ChangedAgain Product",
  "sku": "SKU00967462",
  "description": "desc2",
  "barcode": "8346201275534",
  "brand":"6ecc25c92e8603a5347c648470c11f68",
  "tags": "10ac064c68a8d641d98b798bc0f480f7",
  "vendor": "a248de0582017749e14c3cc4a6395846",
  "stock": 30,
  "reserved": 5,
  "cost": 450.67,
  "basePrice": 259.70,
  "taxPercent": 35, 
  "price": 89.78,
  "weight": 6,
  "active": true,
  "thumbnail": "assets/images/apps/ecommerce/products/watch-01-thumb.jpg",
  "images": "assets/images/apps/ecommerce/products/watch-01-01.jpg"
}
```
