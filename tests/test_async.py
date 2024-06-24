import pytest
import httpx
import asyncio
from starlette.testclient import TestClient
from main import app
from httpx import AsyncClient
from unittest import mock


async def test_async_judicatura():
    async with AsyncClient(app=app, base_url="http://test") as client:

        async def hit_api():
            with mock.patch("fastapi.BackgroundTasks.add_task") as mock_add_task:
                response = await client.post(
                    "/scrapper",
                    json={
                        "actor_id": "0968599020001",
                        "demandado_id": "",
                    },
                )
                return response

        tasks = [asyncio.create_task(hit_api()) for _ in range(15)]
        task_api_async = await asyncio.gather(*tasks)
        for task in task_api_async:
            assert task.status_code == 200
