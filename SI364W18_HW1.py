## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".



## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
import requests
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def welcome():
    return "Welcome to SI 364!"

@app.route('/movie/<moviename>')
def movie(moviename):
    baseurl = 'https://itunes.apple.com/search?'
    params = {"term": moviename, 'media':'movie', 'limit': '1'}
    r = requests.get(baseurl, params = params)
    return r.text

@app.route('/question')
def question():
    q = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/double" method='POST'>
Enter your favorite number:<br>
<input type="text" name="number"><br>
<input type="submit" value="Submit">
</form>

</body>
</html>"""
    return q

@app.route('/double', methods=['POST'])
def double():
    d = int(request.form["number"])
    try:
        return "Double your favorite number is {}".format(d*2)
    except:
        return "Something got fucked"

@app.route('/problem4form', methods=['GET','POST'])
def problem4():
    formstring = """<!DOCTYPE html>
    <html>
    <body>
    <form method='POST'>
    Type in a movie:<br>
    <input type="text" name="movie"><br><br>

    Rate the movie out of 10:<br>
    <input type="checkbox" name="userrating" value:"1"> 1<br>
    <input type="checkbox" name="userrating" value:"2"> 2<br>
    <input type="checkbox" name="userrating" value:"3"> 3<br>
    <input type="checkbox" name="userrating" value:"4"> 4<br>
    <input type="checkbox" name="userrating" value:"5"> 5<br>
    <input type="checkbox" name="userrating" value:"6"> 6<br>
    <input type="checkbox" name="userrating" value:"7"> 7<br>
    <input type="checkbox" name="userrating" value:"8"> 8<br>
    <input type="checkbox" name="userrating" value:"9"> 9<br>
    <input type="checkbox" name="userrating" value:"10"> 10<br>

    <br>

    Click submit to find out its rating on IMDb!<br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>"""

    if request.method == 'POST':
        movie = request.form.get('movie', "")
        baseurl = "http://www.omdbapi.com/?apikey=b95d25d9&"
        params = {"t": request.form['movie'], "type": "movie", "plot": "full", "r": "json"}
        r = requests.get(baseurl, params = params)
        data = json.loads(r.text)

        print ("<br>Your rating is " + request.form.get('userrating') + ". " + "The IMDb rating is  " + data["imdbRating"] + "<br><br>" + formstring)

        print (request.form["userrating"])

        return "<br>The IMDb rating for " + request.form.get('movie') + " is  " + data["imdbRating"] + ".<br><br>" + formstring
    else:
        return formstring



if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

# @app.route('/seeform', methods=['GET','POST'])
# def see_form():
#   formstring = """<br><br>
#   <form action="http://localhost:5000/seeform" method='POST'>
#   Enter a phrase: <br>
#   <input type="text" name="phrase">
#   <input type="submit" value="Submit">"""

#   if request.method == 'POST':
#       entered = request.form.get('phrase', "")
#       return "The last phrase entered was {}".format(entered) + formstring
#   else:
#       return formstring


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
