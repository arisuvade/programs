package practice;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame5 {

    static Scanner scanner = new Scanner(System.in);
    static ArrayList<Integer> guesses = new ArrayList<>();
    static int guess;

    public static void main(String[] args) {

        Random random = new Random();

        int number = random.nextInt(10);
        int limit = 5;

        while (true) {

            getGuess();

            // Correct
            if (guess == number) {
                System.out.println("Correct! It's " + number);
                break;
            }

            // Wrong | Out of guesses
            limit--;
            if (limit == 0) {
                System.out.println("Out of guesses! It's " + number);
                break;
            }

            // Clues | Hints
            if (guess > number) {
                System.out.println("Lower!");
            } else {
                System.out.println("Higher!");
            }

            // Reminder of number of guess left
            System.out.println((limit > 0) ? limit + " guesses left" : "1 guess left only");

        }

        scanner.close();

    }

    private static int getGuess() {

        while (true) {

            // Checking #1 - Check if the input is a whole number
            try {
                System.out.print("Guess: ");
                guess = scanner.nextInt();
            } catch (InputMismatchException ime) {
                scanner.nextLine();
                System.out.println("Invalid input");
                continue;
            }

            // Checking #2 - Check if the guess is in range
            if (guess < 0 || guess > 9) {
                System.out.println("Guess 0-9 only");
                continue;
            }

            // Checking #3 - Check if guess is said already
            if (guesses.contains(guess)) {
                System.out.println("You've already tried " + guess);
                continue;
            }
            guesses.add(guess);

            return guess;
        }

    }

}
