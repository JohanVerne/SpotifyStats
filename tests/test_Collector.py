import pytest
import statsCollector


def test_import_spotify_client():
    spClient = statsCollector.setup_spotify_client()
    assert spClient is not None
    # Check that the client has the expected method
    assert hasattr(spClient, "current_user")
