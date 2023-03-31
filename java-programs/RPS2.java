package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class RPS2 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        ArrayList<String> choices = new ArrayList<>(Arrays.asList("rock", "paper", "scissors"));
        String comChoice = choices.get(random.nextInt(3));
        String userChoice;

        System.out.println("Rock, Paper, and Scissors");
        while (true) {
            System.out.print("User: ");
            userChoice = scanner.nextLine().toLowerCase();

            if (!choices.contains(userChoice)) {
                continue;
            }
            scanner.close();
            System.out.println("Com: " + comChoice);

            if (userChoice.equals(comChoice)) {
                System.out.println("Draw!");
            } else if ((userChoice.equals("rock") && comChoice.equals("scissors"))
                    || (userChoice.equals("paper") && comChoice.equals("rock"))
                    || (userChoice.equals("scissors") && comChoice.equals("paper"))) {
                System.out.println("You won!");
            } else {
                System.out.println("You loss!");
            }

            break;
        }

    }

}