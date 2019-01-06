from flask import Blueprint,render_template,request,jsonify
import requests,json

# creating a Blueprint class
search_blueprint = Blueprint('search',__name__,template_folder="templates")
search_term = ""


headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}

@search_blueprint.route("/",methods=['GET','POST'],endpoint='index')
def index():
    if request.method=='GET':
        return render_template("search.html")
    elif request.method =='POST':

        search_term = request.form["input"]
        print("POST request called")
        print(search_term)
        payload ={
          "autocomplete" : {
            "text" : str(search_term),
            "completion" : {
              "field" : "title_suggest"
            }
          }
        }
        payload = json.dumps(payload)
        url="http://localhost:9200/autocomplete/_suggest"
        response = requests.request("GET", url, data=payload, headers=headers)
        response_dict_data = json.loads(str(response.text))
        return json.dumps(response_dict_data)

@search_blueprint.route("/result",methods=['GET','POST'],endpoint='search_result')
def search_result():
    if request.method == 'POST':
        print("-----------------Calling search Result----------")
        search_term = request.form["input"]
        print("Search Term:",search_term)
        payload = {
            "query": {
                "multi_match": {
                    "query": str(search_term),
                    "fields": ["topic", "title", "url", "labels"]
                }
            },
            "sort": [
                {"upvote": {"order": "desc"}}
            ]
        }
        payload = json.dumps(payload)
        url = "http://localhost:9200/hacker/tutorials/_search"
        response = requests.request("GET", url, data=payload, headers=headers)
        response_dict_data = json.loads(str(response.text))
        return render_template('results.html', res=response_dict_data )


@search_blueprint.route("/test",methods=['GET','POST'],endpoint='test')
def test():
    return render_template("test.html")