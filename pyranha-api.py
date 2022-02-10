#!/usr/bin/env python

from flask import Flask, abort, jsonify, request

interactions = [
    ('happy', 'Happyranha can be nice but being away is an advice.'),
    ('angry', 'Happyranha is angry but what to expect frankly.'),
    ('indifferent', 'Happyranha doesn\'t care but getting closer you shouldn\'t dare.'),
    ('hungry', 'Happyranha now is hungry and you started to look chunky.'),
]

app = Flask(__name__)

@app.route('/')
def index():
    return f"""<html>
<head>
</head>
    <body>
    <h1>Pyranha API</h1>
    <p>This application doesn't do much, but it bites! </p>
    <p>
        <img src="https://thedrawingjourney.com/wp-content/uploads/2019/04/how-to-draw-a-piranha-step-ten.jpeg" alt="pyranha-photo" width="400" height="300">
    </p>
    <h2>Endpoints</h2>
        <ol>
            <li><a href="/ping">/ping</a>
            <li><a href="/healthcheck">/healthcheck</a>
            <li><a href="/moods">/moods</a>
            <li><a href="/replies">/replies</a>
            <li><a href="/pyranha-interaction/{interactions[0][0]}">
              /pyranha-interaction/&lt;happy&gt;</a>
            <li><a href="/interaction_by_mood">/interaction_by_mood</a>
        </ol>
    </body>
</html>"""

def pyranha_debug():
    print({interact[0]: interact[1] for interact in interactions})

def interaction_by_mood():
    return {interact[0]: interact[1] for interact in interactions}

#
#
#
### API METHODS BELOW
#
@app.route('/ping')
def get_ping():
    return f"""<html>
            <head>
            </head>
                <body>
                <h1>Pyranha bites!</h1>
                <p>Sssss...Naaack!! </p>
                </body>
            </html>"""


@app.route('/healthcheck')
def get_healthcheck():
    return jsonify(
        {
            "CustomHealthCheck": {"healthy": True},
            "HttpStatusHealthCheck": {
                "healthy": True,
                "message": "Happyranha swimming in the lake..."
            }
        }
    )


@app.route('/moods')
def get_moods():
    return jsonify([moods[0] for moods in interactions])


@app.route('/replies')
def get_replies():
    return jsonify([replies[1] for replies in interactions])


@app.route('/pyranha-interaction')
def get_default_interaction():
    response = app.make_response("Pyranha says hello, but stay away \'por favor\'.")
    response.mimetype = 'text/plain'
    return response


@app.route('/pyranha-interaction/<mood>')
def get_pyranha_interaction(mood):
    try:
        response = app.make_response(interaction_by_mood()[mood])
        response.mimetype = 'text/plain'
        return response
    except KeyError:
        abort(404)


@app.route('/interaction_by_mood')
def get_interaction_by_mood():
    return jsonify(interaction_by_mood())


if __name__ == '__main__':
    pyranha_debug()
    app.run(host='0.0.0.0', port=8080, debug=True)