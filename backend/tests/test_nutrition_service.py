import pytest
from services.nutrition_service import fetch_nutrition


def test_fetch_nutrition(mocker):
    """
    Test fetching nutrition information using a mocked FDC API response.
    """
    mock_response = {
        "foods": [
            {
                "description": "Apple",
                "foodNutrients": [
                    {"nutrientName": "Energy", "value": 52},
                    {"nutrientName": "Protein", "value": 0.3},
                    {"nutrientName": "Total lipid (fat)", "value": 0.2},
                    {"nutrientName": "Carbohydrate, by difference", "value": 14}
                ]
            }
        ]
    }

    mocker.patch("services.nutrition_service.requests.get",
                 return_value=mocker.Mock(json=lambda: mock_response))

    result = fetch_nutrition("apple")

    assert result["ingredient"] == "apple"
    assert result["calories"] == 52
    assert result["protein"] == 0.3
    assert result["fat"] == 0.2
    assert result["carbs"] == 14
