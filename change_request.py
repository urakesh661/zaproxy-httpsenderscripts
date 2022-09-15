import random
import string

OLD_USERNAME = "592g";
NEW_USERNAME = str(random.randint(0, 10));
RANDOM_STRING = random.choice(string.ascii_letters);

def sendingRequest(msg, initiator, helper):
    global OLD_USERNAME;
    global NEW_USERNAME;
    global RANDOM_STRING;

    body = msg.getRequestBody().toString();
    NEW_USERNAME = str(NEW_USERNAME) + RANDOM_STRING
    newbody = body.replace(OLD_USERNAME, NEW_USERNAME);
    msg.setRequestBody(newbody);
    msg.getRequestHeader().setContentLength(msg.getRequestBody().length());
   
def responseReceived(msg, initiator, helper):
    pass;
