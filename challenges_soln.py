from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

#Task 2 : Dynamic URLS 
    #edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
@app.route('/course/<course_name>')
def courseView(course_name):
    return "Welcome to " + course_name

#Task 3.1 Basic HTML Form
    #Set the method and action of the HTML form, such that form data is sent to /result using GET method
    #The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form')
def formView():
    html_form = '''
    <html>
    <body>
    <form method= "POST" action="http://localhost:5000/result">
    <label>Enter an ingredient:
        <input type = "text" name = "ingredient"/>
    </label>
        <input type = "submit" value = "submit"/>
    </form>
    </body>
    </html>
    '''
    return html_form                        

#Task 3.2 : Processing Form Data
@app.route('/result', methods = ['GET', 'POST'])
def resultView():
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results 
    if request.method == "POST":
        ingredient = request.form.get("ingredient")
        params = {}
        params["i"] = ingredient
        response = requests.get("http://www.recipepuppy.com/api/", params = params)
        response_text = json.loads(response.text)
    return str(response_text)

if __name__ == '__main__':
    app.run(debug=True)
