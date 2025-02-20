const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const fetchRecipe = async (data: { ingredients: string[]; servings: string; cuisine: string; preferences?: string }) => {
  try {
    const response = await fetch(`${API_BASE_URL}/generate-recipe`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch recipe");
    }

    return await response.json();
  } catch (error) {
    console.error("Error fetching recipe:", error);
    return null;
  }
};
