import json
import boto3
import datetime

# Initialize AWS clients
comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MovieReviews')

def lambda_handler(event, context):
    # Handle preflight OPTIONS request (CORS)
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps('CORS preflight response')
        }

    try:
        # Parse review from request body
        body = json.loads(event.get('body', '{}'))
        review = body.get('review')
        
        if not review:
            raise ValueError("Missing 'review' in request body")

        # Analyze sentiment
        sentiment = comprehend.detect_sentiment(Text=review, LanguageCode='en')
        result = sentiment['Sentiment']

        # Save result to DynamoDB
        table.put_item(Item={
            'review': review,
            'sentiment': result,
            'timestamp': str(datetime.datetime.now())
        })

        # Log to CloudWatch
        print(f"Review: {review} | Sentiment: {result}")

        # Return response with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'Sentiment': result})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': str(e)})
        }
