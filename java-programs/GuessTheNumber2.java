package Exercises;

import java.util.Random;

import javax.swing.JOptionPane;

public class GuessTheNumber2 {

	public static void main(String[] args) {

		Random random = new Random();

		int limit = 5;
		int number = random.nextInt(10);

		while (limit > 0) {
			int guess = Integer.parseInt(JOptionPane.showInputDialog("Guess:"));

			if (guess > number) {
				JOptionPane.showMessageDialog(null, guess + " is too high!");
			} else if (guess < number) {
				JOptionPane.showMessageDialog(null, guess + " is too low!");
			} else {
				break;
			}
			limit--;
		}

		if (limit == 0) {
			JOptionPane.showMessageDialog(null, "You're out of guesses, try again.");
		} else {
			JOptionPane.showMessageDialog(null, number + " is correct!");
		}

	}

}
