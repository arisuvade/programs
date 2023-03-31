package Exercises;

import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {

	public static void main(String[] args) {

		Random random = new Random();
		Scanner scanner = new Scanner(System.in);

		int limit = 5;
		int number = random.nextInt(10);
		int guess;

		while (limit > 0) {
			System.out.print("Guess: ");
			guess = scanner.nextInt();

			if (guess > number) {
				System.out.println("Too high!");
			} else if (guess < number) {
				System.out.println("Too low!");
			} else {
				break;
			}
			limit--;
		}

		if (limit == 0) {
			System.out.println("You're out of guess. Try again.");
		} else {
			System.out.println("Correct!");
		}

		scanner.close();

	}

}
