from flask import Flask,render_template,request,jsonify
from pymongo import MongoClient
import bot2 as bot2


# headings = ("Food name", "Carbohydrate", "Protein", "Fats", "Fiber")
# data = (
#     ("Apple","32","21","11","9"),
#     ("Orange","3","1","14","19"),
#     ("Pinepple","23","8","21","13"),
#     ("Guava","12","21","11","19"),
#     ("Grapes","32","30","1","4"),

# )


# Connect to MongoDB
mongo_uri = "mongodb+srv://jangra2609:1234@cluster101.jhizg9j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster101"
client = MongoClient(mongo_uri)
db_name = "food_data"
collection_name = "nutrient_level_new"
my_collection = client[db_name][collection_name]

app = Flask(__name__)

@app.route("/",methods=['GET'])
def root():
    return render_template('home.html')

@app.route("/home",methods=['GET'])
def root_home():
    return render_template('home.html')


@app.route("/recipe",methods=['GET'])
def root_recipe():
    return render_template('recipe_content.html')

@app.route("/nutrient",methods=['GET'])
def root_nutrient():
    db_cursors = my_collection.find()
    return render_template('nutrient_value.html', mongo_data = db_cursors)


@app.route("/bot",methods=['POST'])
def calc():
    data_obtained = request.json
    result = bot2.get_result(data_obtained)
    return jsonify(result)



if (__name__) == "__main__":
    app.run(debug=True)