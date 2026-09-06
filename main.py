from flask import *

app=Flask('Project')

@app.Route('/')
def index():
  return render_template('index.html')


app.run()
