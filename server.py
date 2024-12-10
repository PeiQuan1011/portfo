from flask import Flask, render_template, url_for, request, redirect
import csv

# flask can automatically convert the return string to html so that the browser can understand it
# use flask debug mode can detect and make changes in webpage ASAP while off debug mode cannot
# flask link with css and js files gonna put them into a folder name static

# use flask class to instantiate it to app
# __name__ == __main__ currently running main file
app = Flask(__name__)

# just contain a link with root but can't reponse to other route like 'xxx/blogs' instead of 'xxx/'
# if contain same route, it will run the first route it met
# render_template function will search those files in folder named 'templates', so need to put files into it
# render templates use to import html into it so that we can code html intead of output string
# render_templates allow multiple html files working together
# <username> use to pass on the variable dynamically and others variable rules specific to data types
@app.route('/')
def home1():
    return render_template('index.html')

# rewrite many html invocation above is not efficient, need to make dynamic
# let the string be a variable which can be dynamically jump to other html without create it particularly
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    # mode a for appending data into the existing text file
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    # mode a for appending data into the existing text file
    # to avoid adding newline for each row, should set newline as '' here
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # request data which all in form of dictionary
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again!'