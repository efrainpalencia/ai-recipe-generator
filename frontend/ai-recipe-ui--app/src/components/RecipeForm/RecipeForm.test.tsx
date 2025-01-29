import ReactDOM from "react-dom";
import RecipeForm from "./RecipeForm";

it("It should mount", () => {
  const div = document.createElement("div");
  ReactDOM.render(<RecipeForm />, div);
  ReactDOM.unmountComponentAtNode(div);
});
