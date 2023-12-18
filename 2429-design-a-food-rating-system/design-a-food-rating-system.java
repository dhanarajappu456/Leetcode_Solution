import java.util.*;

public class FoodRatings {
    
    Map<String, String> food_cus = new HashMap<>();
    Map<String, Integer> food_rat = new HashMap<>();
    Map<String, TreeSet<Pair<Integer, String>>> cus_food = new HashMap<>();

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {

        for (int i = 0; i < foods.length; i++) {
            String f = foods[i], c = cuisines[i];
            int r = ratings[i];

            food_cus.put(f, c);
            food_rat.put(f, -r);

            cus_food.computeIfAbsent(c, (k) -> new TreeSet<>((a, b) -> {
                int compareVal = Integer.compare(a.getKey(), b.getKey());
                if (compareVal == 0) {
                    return a.getValue().compareTo(b.getValue());
                }
                return compareVal;
            })).add(new Pair<>(-r, f));
        }
    }

    public void changeRating(String food, int newRating) {

        String cus = food_cus.get(food);
        Integer old_rat = food_rat.get(food);
        Pair<Integer, String> oldElement = new Pair<>(old_rat, food);
        cus_food.get(cus).remove(oldElement);
        cus_food.get(cus).add(new Pair<>(-newRating, food));
        food_rat.put(food, -newRating);
    }

    public String highestRated(String cuisine) {
       
        return cus_food.get(cuisine).first().getValue();
    }

}
