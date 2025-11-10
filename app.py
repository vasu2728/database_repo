from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from shapely.wkb import loads as load_wkb
from shapely.geometry import LineString, mapping
import json

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="osm_project",
    user="postgres",
    password="5320",
    host="localhost",
    port="5432"
)

@app.route('/route')
def route():
    lon1 = float(request.args.get('lon1'))
    lat1 = float(request.args.get('lat1'))
    lon2 = float(request.args.get('lon2'))
    lat2 = float(request.args.get('lat2'))

    cur = conn.cursor()

    # Snap to nearest graph vertex
    cur.execute("""
        SELECT id FROM roads_routable_vertices_pgr
        ORDER BY the_geom <-> ST_SetSRID(ST_Point(%s, %s), 4326)
        LIMIT 1
    """, (lon1, lat1))
    start = cur.fetchone()[0]

    cur.execute("""
        SELECT id FROM roads_routable_vertices_pgr
        ORDER BY the_geom <-> ST_SetSRID(ST_Point(%s, %s), 4326)
        LIMIT 1
    """, (lon2, lat2))
    end = cur.fetchone()[0]

    # Run Dijkstra and return geometry as WKB hex
    cur.execute("""
        SELECT ST_AsBinary(way) AS geom
        FROM pgr_dijkstra(
            'SELECT id, source, target, cost, reverse_cost FROM roads_routable',
            %s, %s, directed := true
        ) AS route
        JOIN roads_routable r ON route.edge = r.id;
    """, (start, end))

    rows = cur.fetchall()

    if not rows:
        return jsonify({"error": "No route found"})

    # Convert WKB and build line
    lines = [load_wkb(bytes(row[0])) for row in rows]

    full_route = LineString([pt for line in lines for pt in line.coords])

    geojson = {
        "type": "Feature",
        "geometry": mapping(full_route),
        "properties": {}
    }

    return jsonify(geojson)



if __name__ == '__main__':
    app.run(debug=True)
