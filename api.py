from flask import Flask, request, jsonify,redirect,url_for
import json
from crawler.crawler.handler import get_data

application = Flask(__name__)


@application.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


@application.route('/')
def home():
    resp = {
        "allowed apis": [
            {"endpoint": "/article",
             "method": "get",
             "query_params": ["url", "author", "title", "short_title", "content", "summary", "category", "limit"],
             "query type":"case insensitive regex matching query",
             "example":[
                 "www.host.com/article",
                 "www.host.com/article?limit=2",
                 "www.host.com/article?author=facebook&category=india"
             ]
             }
        ]
    }
    return jsonify(resp)


@application.route('/article')
def get_article():
    resp = get_data(request.args)
    resp = json.loads(resp)
    if not resp:
        resp = {"msg": "Data Not Found"}
    return jsonify(resp)



if __name__ == '__main__':
    application.run(host='0.0.0.0')
