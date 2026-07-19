import json

def lambda_handler(event, context):
    try:
        # Parse the request body
        body = json.loads(event.get('body', '{}'))
        print("Received data:", body)

        # Get the 'name' field from the request body
        # If it doesn't exist, use "User" as the default value
        name = body.get('name', 'User')

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': json.dumps(f"Hi {name}, your form has been submitted successfully! 🎉")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps("An error occurred while processing your request.")
        }
