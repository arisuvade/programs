package practice;

import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class NumberGuessingGame6 {

    public static void main(String[] args) {

        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        // The answer
        final int ANSWER = random.nextInt(10);

        // The user's guess
        int guessNumber;

        // The limit of guesses
        final int LIMIT = 5;

        // The range of the guess answer
        final int MIN_GUESS = 0;
        final int MAX_GUESS = 9;

        // The checker of number is said already
        Set<Integer> guesses = new HashSet<>();

        // Start of the game
        for (int guessCount = 0; guessCount < LIMIT;) {

            // Checking #1 - Check if the input is a whole number
            try {
                System.out.print("Guess: ");
                guessNumber = scanner.nextInt();
            } catch (InputMismatchException ime) {
                scanner.nextLine();
                System.out.println("Invalid input");
                continue;
            }

            // Checking #2 - Check if the guess is in range
            if (guessNumber < MIN_GUESS || guessNumber > MAX_GUESS) {
                System.out.println("Guess 0-9 only");
                continue;
            }

            // Checking #3 - Check if guess is said already
            if (guesses.contains(guessNumber)) {
                System.out.println("You've already tried " + guessNumber);
                continue;
            }
            guesses.add(guessNumber);

            // Correct
            if (guessNumber == ANSWER) {
                System.out.println("Correct! It's " + ANSWER);
                break;
            }

            // Wrong | Out of guesses
            guessCount++;
            if (guessCount == 5) {
                System.out.println("Out of guesses! It's " + ANSWER);
                break;
            }

            // Clues | Hints
            if (guessNumber > ANSWER) {
                System.out.println("Lower!");
            } else {
                System.out.println("Higher!");
            }

            // Reminder of number of guess left
            System.out.println((guessCount < LIMIT) ? (LIMIT - guessCount) + " guesses left" : "1 guess left");
        }

        // Closing the scanner
        scanner.close();

    }

}
