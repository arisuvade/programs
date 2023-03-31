package exercises;

import java.util.Random;
import java.util.Scanner;

public class RPS1 {
	public static void main(String[] args) {

		Random random = new Random();
		Scanner scanner = new Scanner(System.in);

		String[] choices = { "rock", "paper", "scissors" };

		int comChoiceIndex = random.nextInt(choices.length);
		String comChoice = choices[comChoiceIndex];
		String userChoice;

		while (true) {
			System.out.print("User: ");
			userChoice = scanner.next().toLowerCase();
			if (userChoice.equals("rock") || userChoice.equals("paper") || userChoice.equals("scissors"))
				break;
			else
				System.out.println("Rock, Paper, and Scissors only. Not " + userChoice + "!");
		}

		System.out.println("Com: " + comChoice);
		if (userChoice.equals(comChoice))
			System.out.println("Draw!");
		else if ((userChoice.equals("rock") && comChoice.equals("scissors"))
				|| (userChoice.equals("paper") && comChoice.equals("rock"))
				|| (userChoice.equals("scissors") && comChoice.equals("paper")))
			System.out.println("You won!");
		else
			System.out.println("You loss!");

		scanner.close();

	}
}
