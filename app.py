from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db=SQLAlchemy(app)
class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    complete=db.Column(db.Boolean)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return f'Todo {self.title}'
    
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        title=request.form['title']
        new_task=Task(title=title,complete=False)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Une erreur est survenue lors de l\'ajout de la tâche'
    tasks=Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html',tasks=tasks)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/delete/<int:id>')
def delete(id):
    task=Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except Exception:
        return 'Une erreur est survenue lors de la suppression de la tâche'

@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    task=Task.query.get_or_404(id)
    if request.method=='POST':
        task.title=request.form['title']
        try:
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Une erreur est survenue lors de la modification de la tâche'
    return render_template('partials/update_task.html',task=task)
if __name__ == "__main__":
    app.run(debug=True)