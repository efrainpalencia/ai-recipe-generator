import { useState } from "react";
import { fetchRecipe } from "../../api/index";

const RecipeForm = () => {
  const [ingredients, setIngredients] = useState("");
  const [cuisine, setCuisine] = useState("");
  const [preferences, setPreferences] = useState("");
  const [recipe, setRecipe] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await fetchRecipe({
        ingredients: ingredients.split(",").map((ing) => ing.trim()),
        cuisine,
        preferences,
      });

      if (!response || response.error) {
        throw new Error(response?.error || "Failed to fetch recipe.");
      }

      setRecipe(response);
    } catch (err: any) {
      setError(err.message || "Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-lg mx-auto dark:text-white">
      <div>
        <img src="logo.png" alt="Logo" className="mb-4 border-none rounded" />
      </div>
      <h1 className="text-2xl font-bold mb-4">
        Generate a Recipe:{" "}
        <span className="text-2xl font-thin">
          If you're looking for a recipe idea, add your ingredients, cuisine
          type, and preferences below.
        </span>
      </h1>

      {error && (
        <div className="bg-red-500 text-white p-3 rounded mb-4">⚠️ {error}</div>
      )}

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
          className="w-full flex justify-center items-center bg-lime-500 hover:bg-lime-700 text-white p-2 rounded disabled:opacity-50"
          disabled={loading}
        >
          {loading ? (
            <svg
              className="animate-spin h-5 w-5 mr-2 text-white"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 00-8 8h4z"
              ></path>
            </svg>
          ) : (
            "Generate Recipe"
          )}
        </button>
      </form>

      {recipe && (
        <div className="mt-6 p-4 border rounded shadow">
          <h2 className="text-xl font-bold dark:text-white">{recipe.title}</h2>
          <p>
            <strong>Servings:</strong> {recipe.servings}
          </p>
          <p>
            <strong>Prep Time:</strong> {recipe.prep_time}
          </p>
          <p>
            <strong>Cook Time:</strong> {recipe.cook_time}
          </p>

          <h3 className="mt-4 font-bold dark:text-white">Ingredients:</h3>
          <ul className="list-disc pl-4">
            {recipe.ingredients.map((ing: any, index: number) => (
              <li key={index}>
                {ing.quantity} {ing.name} - {ing.calories} kcal
              </li>
            ))}
          </ul>

          <h3 className="mt-4 font-bold dark:text-white">Instructions:</h3>
          <ol className="list-decimal pl-4">
            {recipe.instructions.map((step: string, index: number) => (
              <li key={index}>{step}</li>
            ))}
          </ol>

          {/* ✅ Display Total Nutrition Info */}
          {recipe.total_nutrition && (
            <div className="mt-4 p-4 border rounded bg-gray-100 dark:bg-gray-700">
              <h3 className="text-lg font-bold dark:text-white">
                Total Nutrition Summary:
              </h3>
              <p>
                <strong>Calories:</strong> {recipe.total_nutrition.calories}{" "}
                kcal
              </p>
              <p>
                <strong>Protein:</strong> {recipe.total_nutrition.protein} g
              </p>
              <p>
                <strong>Fat:</strong> {recipe.total_nutrition.fat} g
              </p>
              <p>
                <strong>Carbs:</strong> {recipe.total_nutrition.carbs} g
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default RecipeForm;
