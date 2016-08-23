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

htmlHead = """
<!DOCTYPE html>
<html>
    <title>Signup</title>
    <body>
"""

htmlTail = """
    </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/signup')

class SignupHandler(webapp2.RequestHandler):
    def get(self):
        username = ""
        uError = ""
        pError = ""
        vError = ""
        email = ""
        eError = ""
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
                                <input type="text" name="username">{0}</input>
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
                                <input type="text" name="email">{4}</input>
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

    def post(self):
        username = cgi.escape(self.request.get("username"))
        email = cgi.escape(self.request.get("email"))

        uError = ""
        pError = ""
        vError = ""
        eError = ""

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
                                <input type="text" name="username">{0}</input>
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
                                <input type="text" name="email">{4}</input>
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
        response = htmlHead + htmlTail
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
