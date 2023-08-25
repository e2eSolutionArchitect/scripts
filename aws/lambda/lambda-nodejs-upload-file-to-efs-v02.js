// NodeJS 
import * as fs from 'fs';

export const handler = async (event) => {
  try {
    
    const fileContent = JSON.parse(event.body).content; 
    const filePath = '/mnt/upload/myfile.txt';

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
