from flask import Flask, render_template, request
from searchengine.search_engine import query_elasticsearch

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('/index.html')


@app.route('/search', methods=['POST'])
def search():
    resp_obj = []
    if request.method == 'POST':
        search_query = request.form["search"]
        res = query_elasticsearch(search_query)
        for i in res:
            resp_obj.append(i['_source'])
    return render_template('/index.html', resp_obj=resp_obj, search_query= search_query)


if __name__ == '__main__':
    app.run()
