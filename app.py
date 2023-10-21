from wsgiref import simple_server
from flask import Flask, request,render_template
from flask import Response
from flask_cors import CORS, cross_origin




app = Flask(__name__)
CORS(app)


@app.route('/training')
@cross_origin()

def training_route_client():
    try:
        return Response("Training Successful !")
    except ValueError:
        return Response("Error Occured ! %s" % ValueError)
    except KeyError:
        return Response("Error Occured ! %s"% KeyError)
    except Exception as e:
        return Response("Error Occured ! %s" % e)

  


if __name__ == "__main__":
    app.run(debug=True) 