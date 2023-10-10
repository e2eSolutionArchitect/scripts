const AWS = require('aws-sdk');
const fs = require('fs');
require('dotenv').config();

// Configure AWS SDK
AWS.config.update({
    accessKeyId: process.env.AWS_ACCESS_KEY,
    secretAccessKey: process.env.AWS_ACCESS_SECRET_KEY,
    region: process.env.AWS_REGION
  });

const s3 = new AWS.S3();



const download = async (params) => {
  console.log("Initiating download.....");
  s3.getObject(params, (err, data) => {
    if (err) {
        console.log(err);
      } else {
        //console.log(data.Body.toString());
      }
  
    fs.writeFile(process.env.LOCAL_PATH_TO_SAVE_FILE, data.Body, (writeErr) => {
      if (writeErr) {
        console.error(writeErr);
        return;
      }
      console.log(`File downloaded to ${process.env.LOCAL_PATH_TO_SAVE_FILE}`);
    });
  });
};

  module.exports = { download };