def verify_email(token): # check token from email for verification
    # TODO: open database and get token of specific user, set accountStatus to 1 in database
    dbtoken = None
    if token == dbtoken:
        accountStatus = 1
    else:
        return 200
