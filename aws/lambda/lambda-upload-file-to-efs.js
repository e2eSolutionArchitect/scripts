// NodeJs script
import * as fs from 'fs';

export const handler = async (event) => {
  fs.writeFileSync('/mnt/upload/hello.txt','It is working!!');
  const response = {
    statusCode: 200,
    body: JSON.stringify('Hello from Lambda!'),
  };
  return response;
};
