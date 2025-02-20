import RecipeForm from "./components/RecipeForm/RecipeForm";

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center w-full h-auto justify-center pb-0 pl-0 pr-0 pt-0 mt-0 bg-gray-100 dark:bg-slate-600 overflow-x-hidden ">
      <div className="bg-lime-500 flex w-full justify-center pb-0 pl-0 pr-0 pt-0 mt-0 mb-4">
        <img
          src="ai_logo_v2.png"
          alt="Logo"
          className="w-full max-w-sm border-none"
        />
      </div>
      <RecipeForm />
      <div className="box-lg shadow-lg max-w-full w-full text-center dark:bg-lime-500 dark:text-white">
        <span>©2025 EFAITECH SOLUTIONS</span>
      </div>
    </div>
  );
}

export default App;
