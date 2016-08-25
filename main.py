#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

htmlHead = """
<!DOCTYPE html>
<html>
    <style>
        .error {
            color: #f00;
        }
    </style>
    <title>Signup</title>
    <body>
"""

htmlTail = """
    </body>
</html>
"""

# Herein lies the ill-understood voodoo black magic of regular expressions
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_username(username):
    return USER_RE.match(username)
def valid_password(password):
    return PASSWORD_RE.match(password)
def valid_email(email):
    return EMAIL_RE.match(email)

# This redirects from root to the desired url
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/signup')

# Handles everything signup related.
class SignupHandler(webapp2.RequestHandler):
    # This is for the initial get request population of the site.
    def get(self):
        form = """
        <div id="form">
            <h1>Signup:</h1>
            <form method="POST" action="/signup">
                <table>
                    <tbody>
                        <tr>
                            <td>
                                <label for="username">Username:</label>
                            </td>
                            <td>
                                <input type="text" name="username"></input>
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="password">Password:</label>
                            </td>
                            <td>
                                <input type="password" name="password"></input>
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="verify">Verify Password:</label>
                            </td>
                            <td>
                                <input type="password" name="verify"></input>
                                <span class="error"></span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="email">Email (optional):</label>
                            </td>
                            <td>
                                <input type="text" name="email"></input>
                                <span class="error"></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <input type="submit"/>
            </form>
        </div>
        """
        response = htmlHead + form + htmlTail
        self.response.write(response)

    def post(self):
        username = cgi.escape(self.request.get("username"), quote=True)
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = cgi.escape(self.request.get("email"), quote=True)

        # Zeroing variables, in case no errors trip.
        uError = ""
        pError = ""
        vError = ""
        eError = ""

        # Username is empty
        if not username:
            uError = "This is not a valid username"
        # Username is invalid
        elif not valid_username(username):
            uError = "This is not a valid username"
        # Password is empty
        if not password:
            pError = "This is not a valid password"
        # Password is invalid
        elif not valid_password:
            pError = "This is not a valid password"
        # Password and verify don't match
        if password != verify:
            vError = "The passwords do not match"
        # Email is invalid
        if not valid_email(email):
            eError = "This is not a valid email"

        # Redirects the user if there are no errors.
        if not uError and not pError and not vError and not eError:
            self.redirect("/welcome?username={}".format(username))
            return

        form = """
        <div id="form">
            <h1>Signup:</h1>
            <form method="POST" action="/signup">
                <table>
                    <tbody>
                        <tr>
                            <td>
                                <label for="username">Username:</label>
                            </td>
                            <td>
                                <input type="text" name="username" value="{0}"></input>
                                <span class="error">{1}</span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="password">Password:</label>
                            </td>
                            <td>
                                <input type="password" name="password"></input>
                                <span class="error">{2}</span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="verify">Verify Password:</label>
                            </td>
                            <td>
                                <input type="password" name="verify"></input>
                                <span class="error">{3}</span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="email">Email (optional):</label>
                            </td>
                            <td>
                                <input type="text" name="email" value="{4}"></input>
                                <span class="error">{5}</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <input type="submit"/>
            </form>
        </div>
        """.format(username,uError,pError,vError,email,eError)
        response = htmlHead + form + htmlTail
        self.response.write(response)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        name = cgi.escape(self.request.get("username"))
        welcome = """<h1>Welcome, {}!</h1>
        """.format(name)
        response = htmlHead + welcome + htmlTail
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
