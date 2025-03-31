import logging
import platform
import sys
from threading import Timer
import datetime

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

OUTPUT_TOPIC = 'test/topic_results'

def get_input_topic(context):
    try:
        print("inside get input topic ")
        topic = context.client_context.custom['subject']
        print("topic is: " + topic)
    except Exception as e:
        logging.error('Topic could not be parsed. ' + repr(e))
    return topic

def getList(dict):
    return


def get_input_message(event):
    print("inside get input message ")
    try:
        message = event['message'] + ', Sequence: ' + str(event['sequence']) + ', from:' + event['source']
    except Exception as e:
        logging.error('Message could not be parsed. ' + repr(e))
    return message

def function_handler(event, context):
    try:
        today = datetime.datetime.now()
        date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
        input_topic = get_input_topic(context)
        input_message = get_input_message(event)
        response = 'HW3Group_Core Invoked on topic "%s" with message "%s" at "%s"' % (input_topic, input_message,date_time)
        logging.info(response)
    except Exception as e:
        logging.error(e)

    client.publish(topic=OUTPUT_TOPIC, payload=response)

    return
