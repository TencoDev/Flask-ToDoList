# Imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Flask App
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
database = SQLAlchemy(app)

# Class for Data
class MyTask(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.String(100), nullable=False)
    completed = database.Column(database.Integer, default=0)
    created = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task {self.id}"



with app.app_context():
    database.create_all()

# Home Page
@app.route("/", methods=["POST", "GET"])
def index():
    # Add a Task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            database.session.add(new_task)
            database.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)
    





# Delete an item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        database.session.delete(delete_task)
        database.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error: {e}"
    
# Edit an item
@app.route("/edit/<int:id>", methods = ['GET', 'POST'])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            database.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error as {e}"
    else:
        return render_template("edit.html" , task=task)





if __name__ == "__main__":
    app.run(debug=True)
