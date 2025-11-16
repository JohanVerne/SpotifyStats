# Simple API used to access stats via HTTP requests
from flask import Flask, jsonify, redirect, Response, request
from io import BytesIO
import sys

sys.path.append("..")
import statsCollector
import statsImageGenerator

app = Flask(__name__)


@app.route("/json")  # Endpoint to get Spotify stats as json
def get_stats():
    stats = statsCollector.main()
    return jsonify(stats)


@app.route("/stats")  # Endpoint to get infographics stats
def create_stats_image():
    stats = statsCollector.main()
    requestedContentType = request.args.get("type", None)
    if requestedContentType not in [
        "artists",
        "top_songs",
        "last_albums",
    ]:
        requestedContentType = "artists"
    requestedContentTimerange = request.args.get("range", None)
    if requestedContentTimerange not in ["short_term", "long_term"]:
        requestedContentTimerange = "short_term"
    svgImage = statsImageGenerator.create_spotify_infographic(
        stats, requestedContentType, requestedContentTimerange
    )
    return Response(svgImage, mimetype="image/svg+xml")


@app.route("/")  # Home endpoint
def home():
    return redirect("https://github.com/JohanVerne/SpotifyREADMEStats")


if __name__ == "__main__":
    pass  # For Vercel deployment
