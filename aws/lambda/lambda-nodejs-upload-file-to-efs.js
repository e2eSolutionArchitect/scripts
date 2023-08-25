// NodeJs script
// Pre-requisite: The lambda should be attached to VPC and the File System should be attached also. 
// File system should have accesspoint /mnt/upload/ created already 
// API gateway should have mapping templated defined for content type 'multipart/form-data' - When there are no templates defined (recommended)

import * as fs from 'fs';


export const handler = async (event) => {
  try {
    let filename = event['params']['header']['filename']
    const fileContent = event['body-json'];
    const filePath = '/mnt/upload/'+filename;

    fs.writeFileSync(filePath, fileContent);

    const response = {
      statusCode: 200,
      body: JSON.stringify('File uploaded successfully')
    };

    return response;
    
  } catch (error) {
    console.error('Error uploading file:', error);
    const errorResponse = {
      statusCode: 500,
      body: JSON.stringify('Error uploading file')
    };

    return errorResponse;
  }
};

