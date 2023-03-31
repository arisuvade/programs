package practice;

import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors4 {

    public static void main(String[] args) {

        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        // Choices
        String[] choices = { "Rock", "Paper", "Scissors" };

        // Computer's choice
        final int COM_CHOICE_INDEX = random.nextInt(3);
        String comChoice = choices[COM_CHOICE_INDEX];

        // User's choice index
        int userChoiceIndex;

        // Result of the game
        String result;

        // To play again
        String playAgain;

        while (true) {

            // Guide
            System.out.println("[1] Rock");
            System.out.println("[2] Paper");
            System.out.println("[3] Scissors");

            // Error catcher #1 & #2
            try {
                System.out.print("Choice: ");
                userChoiceIndex = scanner.nextInt() - 1;

                // Display choices
                System.out.println("Com: " + comChoice);
                System.out.println("User: " + choices[userChoiceIndex]);

                // Trigger exception
                if (userChoiceIndex < 0) {
                    throw new ArrayIndexOutOfBoundsException();
                }

            } catch (InputMismatchException ime) {
                System.out.println("Invalid input");
                continue;
            } catch (ArrayIndexOutOfBoundsException aioobe) {
                System.out.println("Invalid choice");
                continue;
            } finally {
                scanner.nextLine();
            }

            // Error catcher #3
            if (userChoiceIndex == COM_CHOICE_INDEX) {
                result = "Draw!";
            } else if ((userChoiceIndex == 0 && COM_CHOICE_INDEX == 2)
                    || (userChoiceIndex == 1 && COM_CHOICE_INDEX == 0)
                    || (userChoiceIndex == 2 && COM_CHOICE_INDEX == 1)) {
                result = "You won!";
            } else {
                result = "You loss!";

            }

            // Display result
            System.out.println("Result: " + result);

            while (true) {

                System.out.println("Play again [y/n]? ");
                playAgain = scanner.next().toLowerCase();

                if (playAgain.equals("y")) {
                    break;
                } else if (playAgain.equals("n")) {
                    scanner.close();
                    System.exit(0);
                } else {
                    System.out.println("Invalid choice");
                    continue;
                }

            }

        }

    }

}
