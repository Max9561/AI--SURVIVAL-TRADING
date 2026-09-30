from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

        assert response.status_code == 200
            assert response.json()["status"] == "online"


            def test_health():

                response = client.get("/health")

                    assert response.status_code == 200
                        assert response.json()["status"] == "healthy"


                        def test_status():

                            response = client.get("/status")

                                assert response.status_code == 200
                                    assert response.json()["backend"] == "online"