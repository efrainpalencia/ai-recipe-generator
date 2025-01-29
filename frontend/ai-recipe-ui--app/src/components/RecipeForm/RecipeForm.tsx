import { useState } from "react";
import { fetchRecipe } from "../../api/index";

const RecipeForm = () => {
  const [ingredients, setIngredients] = useState("");
  const [cuisine, setCuisine] = useState("");
  const [preferences, setPreferences] = useState("");
  const [recipe, setRecipe] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetchRecipe({
      ingredients: ingredients.split(",").map((ing) => ing.trim()),
      cuisine,
      preferences,
    });
    console.log("Response:", response);
    setRecipe(response);
  };

  return (
    <div className="max-w-lg mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Generate a Recipe</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          placeholder="Ingredients (comma separated)"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <input
          type="text"
          placeholder="Cuisine Type"
          value={cuisine}
          onChange={(e) => setCuisine(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <input
          type="text"
          placeholder="Preferences (optional)"
          value={preferences}
          onChange={(e) => setPreferences(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded"
        >
          Generate Recipe
        </button>
      </form>

      {recipe && (
        <div className="mt-6 p-4 border rounded shadow">
          <h2 className="text-xl font-bold">{recipe.title}</h2>
          <p>
            <strong>Servings:</strong> {recipe.servings}
          </p>
          <p>
            <strong>Prep Time:</strong> {recipe.prep_time}
          </p>
          <p>
            <strong>Cook Time:</strong> {recipe.cook_time}
          </p>
          <h3 className="mt-4 font-bold">Ingredients:</h3>
          <ul className="list-disc pl-4">
            {recipe.ingredients.map((ing: any, index: number) => (
              <li key={index}>
                {ing.quantity} {ing.name}
              </li>
            ))}
          </ul>
          <h3 className="mt-4 font-bold">Instructions:</h3>
          <ol className="list-decimal pl-4">
            {recipe.instructions.map((step: string, index: number) => (
              <li key={index}>{step}</li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
};

export default RecipeForm;
