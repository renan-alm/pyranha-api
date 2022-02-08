#!/usr/bin/env python

from flask import Flask, abort, jsonify, request

teams = [
    ('team-ace', 'd3a3f238-37e1-4770-b548-c7bd16c13477'),
    ('team-bear', 'a5af0f63-173a-4671-a3a0-2ad752d1b7c8'),
    ('team-bull', 'af5be6ff-9532-45cf-80d7-8f92c04a9956'),
    ('team-cac', 'a168911c-496c-4e74-a099-12d5feb38550'),
    ('team-cd', '65544467-fac9-4f00-9bf7-3d3e4369e555'),
    ('team-cia', '50f02549-30d6-49b8-abea-d8cfee7b7298'),
    ('team-cloud-squad', 'b023e61c-f05a-4897-b5f2-348b03cd6384'),
    ('team-discover', '62f3c9c2-7e5e-4269-af8e-ce09e1739613'),
    ('team-firefly', '19733a35-1c0a-4ca3-bce3-1ad9ca503040'),
    ('team-frog', '630f47a7-0b09-4526-bb03-53259a611a89'),
    ('team-goat', '318ef137-5d21-4e03-b3de-1022097a45c6'),
    ('team-hodor', '6021e221-3516-41b3-8e74-610e65e93c16'),
    ('team-la', 'e88038c7-ba9f-477c-b28b-0496e47e49b0'),
    ('team-lax', '63f6764f-ea62-43d8-a1ef-087feef5acdd'),
    ('team-mad', '1e35c583-c180-434c-a5f2-9a99cb2a9d77'),
    ('team-mm', '2c13d247-2eb9-47ab-bd0a-3acba794a8bf'),
    ('team-odds', 'd81f2895-0208-4a0b-840d-6786fd240bd0'),
    ('team-pro', '6323dd34-f47d-48ca-9772-f39deb847338'),
    ('team-rad', 'b30ba904-dee5-4a8d-88ad-5a7c6b2cf63f'),
    ('team-shareville', 'ac5dd983-34b8-4f41-83fa-5bfb4022c8d7'),
    ('team-shell', '67260616-87a6-4598-9e2c-f00202719086'),
    ('team-wolf', 'ab340e82-4407-4156-94a0-2378e99b2bba'),
]

app = Flask(__name__)

@app.route('/')
def index():
    return f"""<html>
<head>
</head>
<body>
<h1>service-team-name-translator</h1>
<p>This application allows CD services such as Jenkins and Argo CD to look up
information about teams.</p>
<p>It is not intended for general use, and the CD team may change or even
decommission this application without notice.</p>
<h2>Endpoints</h2>
<ul>
<li><a href="/ping">/ping</a>
<li><a href="/healthcheck">/healthcheck</a>
<li><a href="/team-names">/team-names</a>
<li><a href="/team-uuids">/team-uuids</a>
<li><a href="/team-uuid-by-name/{teams[0][0]}">
  /team-uuid-by-name/&lt;name&gt;</a>
<li><a href="/team-uuids-by-name">/team-uuids-by-name</a>
<li><a href="/team-name-by-uuid/{teams[0][1]}">
  /team-name-by-uuid/&lt;uuid&gt;</a>
<li><a href="/team-names-by-uuid">/team-names-by-uuid</a>
</ul>
</body>
</html>"""


def uuids_by_name():
    return {team[0]: team[1] for team in teams}


def names_by_uuid():
    return {team[1]: team[0] for team in teams}


@app.route('/ping')
def get_ping():
    return 'pong'


@app.route('/healthcheck')
def get_healthcheck():
    return jsonify(
        {
            "CustomHealthCheck": {"healthy": True},
            "HttpStatusHealthCheck": {
                "healthy": True,
                "message": "Don't worry, be happy"
            }
        }
    )


@app.route('/team-names')
def get_team_names():
    return jsonify([team[0] for team in teams])


@app.route('/team-uuids')
def get_team_uuids():
    return jsonify([team[1] for team in teams])


@app.route('/team-uuid-by-name/<name>')
def get_team_uuid_by_name(name):
    try:
        response = app.make_response(uuids_by_name()[name])
        response.mimetype = 'text/plain'
        return response
    except KeyError:
        abort(404)


@app.route('/team-uuids-by-name')
def get_team_uuids_by_name():
    return jsonify(uuids_by_name())


@app.route('/team-name-by-uuid/<uuid>')
def get_team_name_by_uuid(uuid):
    try:
        response = app.make_response(names_by_uuid()[uuid])
        response.mimetype = 'text/plain'
        return response
    except KeyError:
        abort(404)


@app.route('/team-names-by-uuid')
def get_team_names_by_uuid():
    return jsonify(names_by_uuid())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)