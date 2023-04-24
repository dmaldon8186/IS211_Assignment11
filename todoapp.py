from flask import Flask, render_template, request, redirect
app = Flask(__name__)

email_addresses = []
task_list = []
priority_list = []

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    task = request.form['task']
    task_list.append(task)
    priority = request.form['priority']
    priority_list.append(priority)
    print(email_addresses)
    print(task_list)
    print(priority_list)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses = email_addresses, task_list = task_list, priority_list = priority_list)

if __name__ == '__main__':
    app.run()
