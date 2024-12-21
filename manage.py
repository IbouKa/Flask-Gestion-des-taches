from app import app, db,Task

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
        
        task1=Task(title="First Task", complete=False)
        task2=Task(title="Second Task", complete=False)
        task3=Task(title="Third Task", complete=False)
        task4=Task(title="Fourth Task", complete=False)
        db.session.add(task1)
        db.session.add(task2)
        db.session.add(task3)
        db.session.add(task4)
        db.session.commit()
        print('All queries'+str(Task.query.all()))
        
        
