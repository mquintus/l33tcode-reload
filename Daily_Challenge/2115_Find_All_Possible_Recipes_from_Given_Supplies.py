# 2115 - Find All Possible Recipes from Given Supplies
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        ing = [] 
        needing = {recipe: set() for recipe in recipes}
        dependencies = [0] * len(recipes)
        solved = []
        result = []
        for i, r in enumerate(ingredients):
            ing.append(set())
            for req in r:
                if req not in supplies:
                    ing[-1].add(req)
                    if req not in needing:
                        needing[req] = set()
                    needing[req].add(i)
                    dependencies[i] += 1
            if len(ing[-1]) == 0:
                supplies.add(recipes[i])
                solved.append(i)

        while solved:
            some_recipe = solved.pop()
            result.append(recipes[some_recipe])

            for improved_r in needing[recipes[some_recipe]]:
                dependencies[improved_r] -= 1
                if dependencies[improved_r] == 0:
                    solved.append(improved_r)

        return result

            

        

        


        
