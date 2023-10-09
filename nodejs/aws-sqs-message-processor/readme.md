npm install

npm init
npm i @aws-sdk/client-sqs
npm install --save dotenv 
npm install uuid // to generate unique id for message id 

node producer.js
node consumer.js

Create a file .env and paste below values
```
AWS_REGION="us-east-1"
AWS_ACCESS_KEY=##########
AWS_ACCESS_SECRET_KEY=##############
AWS_SQS_QUEUE_URL=################
```
