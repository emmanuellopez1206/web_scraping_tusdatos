from unittest import TestCase, mock
from starlette.testclient import TestClient
from main import app


class TestScrapperApi(TestCase):
    """
    Test Scrapper API
    """

    def setUp(self):
        """
        Configuración inicial para los tests del módulo de usuarios.
        """
        self.client = TestClient(app)

    def tests_api_scrapper_actor(self):
        """
        Test para el endpoint de scrapping
        """
        with mock.patch("fastapi.BackgroundTasks.add_task") as mock_add_task:
            response = self.client.post(
                "/scrapper",
                json={
                    "actor_id": "0968599020001",
                    "demandado_id": "",
                },
            )
            mock_add_task.assert_called_once()
        assert response.status_code == 200

    def tests_api_scrapper_demandado(self):
        """
        Test para el endpoint de scrapping
        """
        with mock.patch("fastapi.BackgroundTasks.add_task") as mock_add_task:
            response = self.client.post(
                "/scrapper",
                json={
                    "actor_id": "",
                    "demandado_id": "1791251237001",
                },
            )
            mock_add_task.assert_called_once()
        assert response.status_code == 200
