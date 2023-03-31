package exercises;

import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber3 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		Random random = new Random();

		int number = random.nextInt(9) + 1;
		int limit = 5;
		int guess;

		while (true) {
			try {
				System.out.print("Guess: ");
				guess = scanner.nextInt();
			} catch (Exception e) {
				scanner.nextLine();
				continue;
			}
			limit--;

			if (limit == 0) {
				System.out.println("Out of guesses. Try again!");
				break;
			}

			if (guess > number)
				System.out.println("Lower!");
			else if (guess < number)
				System.out.println("Higher!");
			else {
				System.out.println("Correct!");
				break;
			}

		}

		scanner.close();

	}

}
