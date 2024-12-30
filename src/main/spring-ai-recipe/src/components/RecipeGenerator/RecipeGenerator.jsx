import React, { useState } from 'react';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/esm/Row';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Spinner from 'react-bootstrap/Spinner';

function RecipeGenerator() {
  const [ingredients, setIngredients] = useState('');
  const [cuisine, setCuisine] = useState('any');
  const [dietaryRestrictions, setDietaryRestrictions] = useState('');
  const [recipe, setRecipe] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const createRecipe = async () => {
    try {
      setIsLoading(true);
      const response = await fetch(
        `http://localhost:8080/recipe-creator?ingredients=${ingredients}&cuisine=${cuisine}&dietaryRestrictions=${dietaryRestrictions}`
      );
      const data = await response.text();
      setRecipe(data);
    } catch (error) {
      console.error('Error generating recipe: ', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <Col>
        <Row className='mb-4 mt-4'>
        <h2 className='text-danger'>Recipe Generator</h2>
        </Row>
        <Form.Label>Ingredients</Form.Label>
        <InputGroup className="mb-3">
          <Form.Control
            placeholder="Enter ingredients (e.g., Salmon, Potatoes, Broccoli)"
            type="text"
            value={ingredients}
            onChange={(e) => setIngredients(e.target.value)}
          />
        </InputGroup>
        <Form.Label>Cuisine</Form.Label>
        <InputGroup className="mb-3">
          <Form.Control
            placeholder="Enter cuisine type"
            type="text"
            value={cuisine}
            onChange={(e) => setCuisine(e.target.value)}
          />
        </InputGroup>
        <Form.Label>Dietary Restrictions</Form.Label>
        <InputGroup className="mb-3">
          <Form.Control
            placeholder="Enter dietary restrictions"
            type="text"
            value={dietaryRestrictions}
            onChange={(e) => setDietaryRestrictions(e.target.value)}
          />
        </InputGroup>
        <div className="d-flex gap-2 mb-4">
          <Button variant="warning" onClick={createRecipe} disabled={isLoading}>
            {isLoading ? (
              <>
                <Spinner as="span" animation="border" size="sm" role="status" aria-hidden="true" />
                <span className="visually-hidden">Loading...</span>
              </>
            ) : (
              'Create Recipe'
            )}
          </Button>
        </div>
        <Card style={{ width: '100%' }}>
          <Card.Body>
            {isLoading ? (
              <div className="text-center">
                <Spinner animation="border" role="status">
                  <span className="visually-hidden">Loading...</span>
                </Spinner>
                <p>Generating your recipe...</p>
              </div>
            ) : (
              <pre>{recipe}</pre>
            )}
          </Card.Body>
        </Card>
      </Col>
    </>
  );
}

export default RecipeGenerator;
