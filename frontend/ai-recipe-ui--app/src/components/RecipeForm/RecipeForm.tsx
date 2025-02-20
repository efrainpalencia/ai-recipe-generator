import { useState } from "react";
import { fetchRecipe } from "../../api/index";

interface CuisineOption {
  value: string;
  label: string;
}
const cuisineOptions: CuisineOption[] = [
  { value: "any", label: "Any" },
  { value: "american", label: "American" },
  { value: "argentine", label: "Argentine" },
  { value: "british", label: "British" },
  { value: "congolese", label: "Congolese" },
  { value: "chinese", label: "Chinese" },
  { value: "cuban", label: "Cuban" },
  { value: "dominicanRepublic", label: "Dominican Republic" },
  { value: "dutch", label: "Dutch" },
  { value: "ethiopian", label: "Ethiopian" },
  { value: "french", label: "French" },
  { value: "german", label: "German" },
  { value: "greek", label: "Greek" },
  { value: "indian", label: "Indian" },
  { value: "japanese", label: "Japanese" },
  { value: "mexican", label: "Mexican" },
  { value: "middleEastern", label: "Middle Eastern" },
  { value: "purtoRican", label: "Puerto Rican" },
  { value: "somali", label: "Somali" },
  { value: "spanish", label: "Spanish" },
  { value: "swahili", label: "Swahili" },
  { value: "tunisian", label: "Tunisian" },
];

interface ServingsOption {
  value: string;
  label: string;
}

const servingsOptions: ServingsOption[] = [
  { value: "1", label: "1 Servings" },
  { value: "2", label: "2 Servings" },
  { value: "3", label: "3 Servings" },
  { value: "4", label: "4 Servings" },
  { value: "5", label: "5 Servings" },
  { value: "6", label: "6 Servings" },
  { value: "7", label: "7 Servings" },
  { value: "8", label: "8 Servings" },
  { value: "9", label: "9 Servings" },
  { value: "10", label: "10 Servings" },
];

const RecipeForm = () => {
  const [ingredients, setIngredients] = useState("");
  const [servings, setServings] = useState("4");
  const [cuisine, setCuisine] = useState("any");
  const [preferences, setPreferences] = useState("");
  const [recipe, setRecipe] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleCuisineChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setCuisine(event.target.value);
  };

  const handleServingsChange = (
    event: React.ChangeEvent<HTMLSelectElement>
  ) => {
    setServings(event.target.value);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await fetchRecipe({
        ingredients: ingredients.split(",").map((ing) => ing.trim()),
        servings,
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
    <div className="flex flex-col items-center w-full min-h-screen max-w-xl pb-3 pl-3 pr-3 pt-6 mt-6 dark:text-white">
      <h1 className="text-2xl font-bold mb-4">
        Are you looking for a recipe idea?{" "}
        <span className="text-2xl font-thin">
          Just add your ingredients, number of servings, cuisine type, and
          preferences below.
        </span>
      </h1>

      {error && (
        <div className="bg-red-500 text-white p-3 rounded mb-4">⚠️ {error}</div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <label>Add Ingredients</label>
        <input
          type="text"
          placeholder="Chicken thighs, lime, cilantro, garlic, avocado..."
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <label htmlFor="servings-select">Select a Serving Size</label>
        <select
          id="servings-select"
          className="bg-gray-100 dark:bg-slate-600 dark:text-white w-full p-2 border rounded"
          value={servings}
          onChange={handleServingsChange}
        >
          <option value="">--Choose a Serving--</option>
          {servingsOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>

        <label htmlFor="cuisine-select">Select a Cuisine</label>
        <select
          id="cuisine-select"
          className="bg-gray-100 dark:bg-slate-600 dark:text-white w-full p-2 border rounded"
          value={cuisine}
          onChange={handleCuisineChange}
        >
          <option value="">--Choose a Cuisine--</option>
          {cuisineOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        <label>Add Preferences</label>
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
            "Generate My Recipe"
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
