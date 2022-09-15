# zaproxy-httpsenderscripts

Problem Statement : Running active scan on a POST request.In my scenario a POST request which allows user registration.

This post request has a validation that if we try to register a user with the same username on each new request,then it will return a response stating that "User already exists" and the user won't be registered.

There has to be a way that new username is generated on each manual execution of active scan.

So modified the change_request.py available at https://github.com/zaproxy/community-scripts/blob/main/httpsender/change_request.py for my scenario.

Usage : Replace the value of OLD_USERNAME variable with the value of username parameter sent in api post request.
