from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

task_list = []

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    task= (request.form['email'], request.form['task'], request.form['priority'])
    if not re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$').match(task[0]):
        print('Email invalid')
        return redirect('/')
    if task[2] not in ['low', 'medium', 'high']:
        print('Priority invalid')
        return redirect('/')
    task_list.append(task)
    print(task_list)
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    task_list.clear()
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', task_list = task_list)

if __name__ == '__main__':
    app.run()