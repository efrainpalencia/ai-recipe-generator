import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_generate_recipe(client, mocker):
    """Test the recipe generation endpoint with mocked OpenAI API response."""
    mock_openai_response = {
        "recipe": "Mock Recipe",
        "ingredients": ["1 cup flour", "2 eggs"],
        "instructions": ["Mix ingredients", "Bake for 20 mins"]
    }

    mocker.patch("services.openai_service.generate_recipe",
                 return_value=mock_openai_response)

    response = client.post("/api/generate-recipe",
                           json={"ingredients": ["flour", "eggs"]})

    assert response.status_code == 200
    data = response.get_json()
    assert "recipe" in data
    assert len(data["ingredients"]) > 0
    assert len(data["instructions"]) > 0
