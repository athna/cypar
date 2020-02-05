#!/bin/env python
import yaml

"""
/*
[content_parser.py]

Copyright (C) 2020 [athna]
License: http://www.gnu.org/licenses/gpl.html GPL version 3 or higher
*/
"""

with open('path/to/content_description.yml') as file:
    obj = yaml.safe_load(file)

print(obj[0]["training"][0]["id"])                                      #training_ID     
print(obj[0]["training"][0]["level"])                                   #training_LEVEL
print(obj[0]["training"][0]["overview"])                                #training_OVERVIEW
for i  in range(len(obj[0]["training"][0]["questions"])):
    print(obj[0]["training"][0]["questions"][i]["id"])                  #ID
    print(obj[0]["training"][0]["questions"][i]["body"])                #BODY
    for j in range(len(obj[0]["training"][0]["questions"][i]["hints"])):#HINTS
        print(obj[0]["training"][0]["questions"][i]["hints"][j])        #HINT
    print(obj[0]["training"][0]["questions"][i]["answer"])              #ANSWER
    print("---")
