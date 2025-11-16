# Create an SVG infographic for the requested content type and time range
def create_spotify_infographic(
    stats_data: dict, section_type: str = "artists", time_range: str = "short_term"
) -> str:
    svg_header = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#121212"/>
    <style>
        .title { fill: #1DB954; font-family: Arial, sans-serif; font-size: 32px; font-weight: bold; }
        .header { fill: #FFFFFF; font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; }
        .text { fill: #FFFFFF; font-family: Arial, sans-serif; font-size: 16px; }
        .subtext { fill: #969696; font-family: Arial, sans-serif; font-size: 14px; }
    </style>
    """

    # Top Artists Section
    if section_type == "artists":
        if time_range == "short_term":  # Get the correct time range artist data
            svg_content = (
                '<text x="20" y="50" class="title">My Recent Top Artists</text>'
            )
            top_artists = stats_data.get("top_artists", {}).get("short_term", {})
        elif time_range == "long_term":
            svg_content = (
                '<text x="20" y="50" class="title">My All-Time Top Artists</text>'
            )
            top_artists = stats_data.get("top_artists", {}).get("long_term", {})
        else:
            return None
        y = 30
        for i, (idx, artist) in enumerate(list(top_artists.items())[:5]):
            name = artist.get("name", "Unknown")
            svg_content += f'<text x="40" y="{y}" class="text">{i+1}. {name}</text>'
            y += 30
            genre = artist.get("genre", "Unknown")
            svg_content += f'<text x="450" y="{y}" class="subtext">({genre})</text>'
            y += 30
            image = artist.get("image", None)
            if image:
                svg_content += (
                    f'<image href="{image}" x="10" y="{y-20}" height="20" width="20"/>'
                )
            else:
                svg_content += f'<image href="images/Spotify.svg" x="10" y="{y-20}" height="20" width="20"/>'

    # Top Songs Section
    elif section_type == "top_songs":
        if time_range == "short_term":  # Get the correct time range song data
            svg_content = '<text x="20" y="50" class="title">My Recent Top Songs</text>'
            top_songs = stats_data.get("top_songs", {}).get("short_term", {})
        elif time_range == "long_term":
            svg_content = (
                '<text x="20" y="50" class="title">My All-Time Top Songs</text>'
            )
            top_songs = stats_data.get("top_songs", {}).get("long_term", {})
        else:
            return None

        y = 30
        for i, (idx, song) in enumerate(list(top_songs.items())[:5]):
            name = song.get("name", "Unknown")
            svg_content += f'<text x="40" y="{y}" class="text">{i+1}. {name}</text>'
            y += 30
            artist_name = song.get("artist", "Unknown")
            svg_content += (
                f'<text x="450" y="{y}" class="subtext">by {artist_name}</text>'
            )
            y += 30
            image = song.get("image", None)
            if image:
                svg_content += (
                    f'<image href="{image}" x="10" y="{y-20}" height="20" width="20"/>'
                )
            else:
                svg_content += f'<image href="images/Spotify.svg" x="10" y="{y-20}" height="20" width="20"/>'

    # Last Played Albums Section
    elif section_type == "last_albums":
        svg_content = (
            '<text x="20" y="50" class="title">My Recently Played Albums</text>'
        )
        last_albums = stats_data.get("last_albums", {})
        y = 30
        for i, (idx, album) in enumerate(list(last_albums.items())[:5]):
            name = album.get("name", "Unknown")
            svg_content += f'<text x="40" y="{y}" class="text">{i+1}. {name}</text>'
            y += 30
            artist_name = album.get("artist", "Unknown")
            svg_content += (
                f'<text x="450" y="{y}" class="subtext">by {artist_name}</text>'
            )
            y += 30
            image = album.get("image", None)
            if image:
                svg_content += (
                    f'<image href="{image}" x="10" y="{y-20}" height="20" width="20"/>'
                )
            else:
                svg_content += f'<image href="images/Spotify.svg" x="10" y="{y-20}" height="20" width="20"/>'

    else:
        return None

    svg_footer = "</svg>"

    # return complete SVG
    return svg_header + svg_content + svg_footer
