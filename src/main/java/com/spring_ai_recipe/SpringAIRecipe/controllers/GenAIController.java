package com.spring_ai_recipe.SpringAIRecipe.controllers;

import com.spring_ai_recipe.SpringAIRecipe.services.RecipeService;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GenAIController {

    RecipeService recipeService;

    public GenAIController(RecipeService recipeService) {
        this.recipeService = recipeService;
    }


    @GetMapping("recipe-creator")
    public String recipeCreator(@RequestParam String ingredients, @RequestParam(defaultValue = "any") String cuisine, @RequestParam(defaultValue = "") String dietaryRestrictions) {
        return recipeService.createRecipe(ingredients, cuisine, dietaryRestrictions);
    }

}
