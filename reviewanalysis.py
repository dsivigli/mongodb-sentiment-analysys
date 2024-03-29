import os, boto3
import logging
import json

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)

ESCALATION_INTENT_MESSAGE="Seems that you are having troubles with our service. Would you like to be transferred to the associate?"
FULFILMENT_CLOSURE_MESSAGE="Seems that you are having troubles with our service. Let me transfer you to the associate."
GOOD_REVIEW_CLOSURE_MESSAGE="We are happy you are satisfied with your choice!"

escalation_intent_name = os.getenv('ESCALATION_INTENT_NAME', None)

client = boto3.client('comprehend')

def lambda_handler(event, context):
    
    logger.info('Event: %s' % json.dumps(event))
   
    sentiment=client.detect_sentiment(Text=event["detail"]["fullDocument"]['review'],LanguageCode='en')['Sentiment']
   
    if sentiment=='NEGATIVE':
        if escalation_intent_name:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                    },
                    "dialogAction": {
                        "type": "ConfirmIntent", 
                        "message": {
                            "contentType": "PlainText", 
                            "content": ESCALATION_INTENT_MESSAGE
                        }, 
                    "intentName": escalation_intent_name
                    }
            }
        else:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                },
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                    "message": {
                            "contentType": "PlainText",
                            "content": FULFILMENT_CLOSURE_MESSAGE
                    }
                }
            }
    else:
        logger.info('Sentiment analysis: %s' % GOOD_REVIEW_CLOSURE_MESSAGE)
        result ={
            "sessionAttributes": {
                "sentiment": sentiment
            },
             "dialogAction": {
                    "type": "ConfirmIntent",
                    "message": {
                            "contentType": "PlainText", 
                            "content": GOOD_REVIEW_CLOSURE_MESSAGE
                        }, 
                    "intentName": escalation_intent_name
            }
        }
        
    return result