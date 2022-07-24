import requests
import os

class CreateUserUserService():

    def __init__(self, email, username):

        self.email = email
        self.username = username

    def create_user(self):

        url = '{0}/insert-user'.format(os.getenv('USER_SERVICE_URL'))
        data = {"email" : self.email,"name" : self.firstName}
        requests.post(url, json = data)