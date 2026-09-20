from app import create_app
def test_health(): assert create_app().test_client().get("/api/health").get_json()["version"]=="1.2.0"
def test_home(): assert b"Materials Lab" in create_app().test_client().get("/").data
