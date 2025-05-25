Movie Review Sentiment Analyzer using AWS

1. About the Project

This project is a cloud-native application that analyzes the sentiment of movie reviews using Amazon Comprehend. The system accepts user reviews from a front-end web interface, determines the sentiment (Positive, Negative, Neutral, or Mixed), stores the review and result in DynamoDB, logs the analysis in CloudWatch, sends the result via Amazon SES, and visually displays the outcome to the user. The application is fully serverless, scalable, and leverages AWS services for natural language processing, storage, logging, and email notification.

2. Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: AWS Lambda (Python)
Cloud Services:
    Amazon API Gateway
    AWS Lambda
    Amazon Comprehend
    Amazon DynamoDB
    Amazon CloudWatch
    Amazon Simple Email Service (SES)


3. Explanation of Each AWS Service

Amazon Comprehend: A Natural Language Processing (NLP) service used to analyze the sentiment of the submitted movie reviews.

Amazon DynamoDB: A NoSQL database used to store the original movie reviews along with their corresponding sentiment analysis results and timestamps.

Amazon API Gateway: Acts as the front-door for the Lambda function, exposing a RESTful API that receives review input from the client-side application.

AWS Lambda: Serverless compute service that hosts the core logic for invoking Amazon Comprehend, storing results in DynamoDB, logging to CloudWatch, and sending email notifications via SES.

Amazon CloudWatch: Used to monitor, log, and troubleshoot the sentiment analysis results and Lambda execution.

Amazon Simple Email Service (SES): Sends automated emails containing the review and its sentiment to a predefined recipient.

4. Merging and Integration of Services
 
Frontend sends review data to an API Gateway endpoint via HTTP POST.
API Gateway routes the request to a Lambda function.
Lambda processes the input by invoking Amazon Comprehend for sentiment analysis.
The sentiment and review are stored in Amazon DynamoDB.
Amazon SES is used to send an email with the sentiment result to the designated recipient.
Amazon CloudWatch logs all relevant data for monitoring and debugging purposes.
The front-end receives the sentiment result and displays it to the user in a user-friendly format.

5. How It Works
 
The user opens the web interface and enters a movie review.
Upon clicking the “Analyze Sentiment” button, a JavaScript function sends the review to the backend via the API Gateway.
API Gateway forwards the request to the Lambda function.
Lambda analyzes the text using Amazon Comprehend, stores the result in DynamoDB, logs the details, and triggers an email via SES.
The Lambda function returns the sentiment result to the front-end.
The front-end displays the sentiment type (Positive, Negative, Neutral, or Mixed) to the user.

6. Conclusion

This project demonstrates the integration of multiple AWS services in a real-time sentiment analysis use case. It showcases how to build a scalable, cost-effective, and fully serverless architecture using Amazon Comprehend, Lambda, DynamoDB, API Gateway, SES, and CloudWatch. The application provides valuable insights into user feedback through automated sentiment detection, making it applicable to various domains including customer reviews, feedback systems, and opinion analysis.

