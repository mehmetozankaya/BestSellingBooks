from flask import Flask, render_template, json, jsonify, Response, request
import db

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/add')
def add():
    return render_template('add.html')
 
@app.route('/getbooks')
def get_books():
    # empty array to store data
    output = []
    query = {"status": 1}
    #get data from MongoDB and store it in the array
    for s in db.table.find(query):
        del s['_id']
        output.append(s)
    #create json object to pass to template
    data = {
        "data": output
    }
    return jsonify(data)

@app.route('/api/create', methods = ['POST', 'GET'])
def create():
    authorName = ""
    bookName = ""
    customersRated = ""
    imageURL = ""
    price = ""
    rating = ""
    status = 1
    entryID = db.table.estimated_document_count()
    if request.method == 'POST':
        authorName = str(request.form['Author'])
        bookName = str(request.form['Book_Name'])
        customersRated = str(request.form['Customers_Rated'])
        imageURL = str(request.form['Imageurl'])
        price = 'CDN$' + str(request.form['Price'])
        rating = str(request.form['Rating']) + ' out of 5 stars'
        entryID = entryID + 1
    
    data = {
        'Book_Name' : bookName,
        'Author' : authorName,
        'Rating' : rating,
        'Customers_Rated': customersRated,
        'Price': price,
        'Imageurl': imageURL,
        'entryID': entryID,
        'status': status
    }

    db.table.insert_one(data)
    return render_template('add.html')

@app.route('/api/update', methods = ['POST', 'GET'])
def update():
    authorName = ""
    bookName = ""
    customersRated = ""
    imageURL = ""
    price = ""
    rating = ""
    status = ""
    entryID = ""
    if request.method == 'POST':
        authorName = str(request.form['Author'])
        bookName = str(request.form['Book_Name'])
        customersRated = str(request.form['Customers_Rated'])
        imageURL = str(request.form['Imageurl'])
        price = 'CDN$' + str(request.form['Price'])
        rating = str(request.form['Rating']) + ' out of 5 stars'
        entryID = int(request.form['entryID'])
        status = int(request.form['status'])
    query = { "entryID": entryID }
    data = { "$set": {
        'Book_Name' : bookName,
        'Author' : authorName,
        'Rating' : rating,
        'Customers_Rated': customersRated,
        'Price': price,
        'Imageurl': imageURL,
        'status': status
    } }
    db.table.update_one(query,data)
    return render_template('index.html')

@app.route('/api/delete', methods = ['POST', 'GET'])
def delete():
    entryID = ""
    if request.method == 'POST':
        entryID = int(request.form['entryID'])
    query = { "entryID": entryID}
    db.table.delete_one(query)
    return render_template('index.html')

@app.route("/about")
def about():
  return render_template("about.html")
#test to insert data to the data base

@app.route("/test")

def test():
    #db.db.forbes_data.insert_one({"name": "John"})
    
    #x = db.db.forbes_data.find({"name": "John"})
    #return "Connected to the database!"
    #print(x)
    output = []
    for s in db.table.find():
        del s['_id']
        output.append(s)
    #print(s)
    #return render_template('index.html', title="page", jsonfile=json.dumps(output))
    return Response(json.dumps(output),  mimetype='application/json')
    #return "Connected to the database!"

if __name__ == '__main__':
    app.run(port=8000)