package Java;

import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber4 {

    public static void main(String[] args) {

        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int number = random.nextInt(1, 10);
        int limit = 5;
        int guess;

        System.out.println("Guess 0 - 9");

        while (true) {
            try {
                System.out.print("Guess: ");
                guess = scanner.nextInt();
                if (guess < 0 || guess > 9) {
                    throw new Exception();
                }
            } catch (InputMismatchException ime) {
                scanner.nextLine();
                System.out.println("That's not a number");
                continue;
            } catch (Exception e) {
                scanner.nextLine();
                System.out.println("Guess 0 to 9 only");
                continue;
            }

            if (guess == number) {
                System.out.println("Correct!");
                scanner.close();
                break;
            } else {
                limit--;
                if (limit == 0) {
                    System.out.println("You're out of guesses");
                    System.out.println("The number is " + number);
                    break;
                } else if (limit == 1) {
                    System.out.println("1 guess left");
                } else {
                    System.out.println(limit + " guesses left");
                }

                if (guess > number) {
                    System.out.println("Lower!");
                } else {
                    System.err.println("Higher!");
                }

            }

        }

    }

}
