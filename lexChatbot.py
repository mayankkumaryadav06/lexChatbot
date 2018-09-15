    try :
        name = event["currentIntent"]["slots"]["Relation"].title()
        #print event["currentIntent"]["slots"]
        if name == "Recruiter" or name == "recruiter" :
            l_response = "Good to see you here. Mayank is talented DevOps Engineer who also likes coding in python. Would you like to know more?"
        elif name == "Friend" or name == "friend" :
            l_response = "Nice. Good to meet his friend. He indeed miss you. Do you have his contact number?"
        response = {
                    "dialogAction":
                        {
                         "fulfillmentState":"Fulfilled",
                         "type":"Close","message":
                            {
                              "contentType":"PlainText",
                              "content": l_response
                            }
                        }
                    }
    except :
        pass

    try:
        print "Hello World"
    except:
        pass
    return response
