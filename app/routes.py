from flask import Blueprint,jsonify,request,render_template
from .scraper import job_scrap 

main = Blueprint("main", __name__)


@main.route("/")
def home():
    
    return render_template("index.html")

@main.route("/status")
def status():
    return jsonify({"status":"running"})

@main.route("/job")
def job():
    query=request.args.get("query","engineer")
    query=query.replace("-"," ").strip().title()

    location=request.args.get("location","lahore")
    try:

        limit=int(request.args.get("limit",5))
    except(TypeError,ValueError):
        limit=5
    

    try:
        page=int(request.args.get("page"))
        if page<1:
            page=1
    except(TypeError,ValueError):
        page=1
    start=(page-1)*limit
    end=start+limit
    results=job_scrap(query,location,end)
    results=results[start:end]


        
    

    
    if not results:
        return jsonify({"message": f"no jobs found for query '{query}' in location '{location}'"})

    return jsonify({
        "page": page,
        "limit": limit,
        "count": len(results),
        "results": results
    })
    