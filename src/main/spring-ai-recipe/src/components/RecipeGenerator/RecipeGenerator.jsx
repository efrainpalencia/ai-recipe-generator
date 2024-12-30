import React, { useState } from 'react';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';


function RecipeGenerator () {
  const [ingredients, setIngredients] = useState('');
  const [cuisine, setCuisine] = useState('any');
  const [dietaryRestrictions, setDietaryRestrictions] = useState('');
  const [recipe, setRecipe] = useState('');

  const createRecipe = async () => {
    try {

      const response = await fetch(`http://localhost:8080/recipe-creator?ingredients=${ingredients}&cuisine=${cuisine}$dietaryRestrictions=${dietaryRestrictions}`)
      const data = await response.text();
      console.log(data);
      setRecipe(data);
      
    } catch (error) {
      console.error("error generating recipe: ", error);
    }
  }

  return (
    <>
    <h2>Create a Recipe</h2>
    <Form.Label>Ingredients</Form.Label>
    <InputGroup className='mb-3'>
    <Form.Control
    placeholder='Enter ingredients (ex: Salmon, Potatoes, Broccoli)'
    type='text'
    value={ingredients}
    onChange={(e) => setIngredients(e.target.value)}
    />
    </InputGroup>
    <Form.Label>Cuisine</Form.Label>
    <InputGroup className='mb-3'>
    <Form.Control
    placeholder='Enter cuisine type'
    type='text'
    value={cuisine}
    onChange={(e) => setCuisine(e.target.value)}
    />
    </InputGroup>
    <Form.Label>Dietary Restrictions</Form.Label>
    <InputGroup className='mb-3'>
    <Form.Control
    placeholder='Enter dietary restrictions'
    type='text'
    value={dietaryRestrictions}
    onChange={(e) => setDietaryRestrictions(e.target.value)}
    />
    </InputGroup>
    <Button variant="outline-primary" onClick={createRecipe}>Create Recipe</Button>
    <div className='output'>
      <pre>{recipe}</pre>
    </div>
    </>
  )

};


export default RecipeGenerator;
