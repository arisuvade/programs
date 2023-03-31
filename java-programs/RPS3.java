package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import javax.swing.JOptionPane;

public class RPS3 {

    public static void main(String[] args) {

        // Terminate the game if don't want to play.
        int wantToPlay = JOptionPane.showConfirmDialog(null, "Do you want to play?", "Rock, Paper, and Scissors!", 0);
        if (wantToPlay != 0) {
            JOptionPane.showMessageDialog(null, "Come and play sometimes!");
            System.exit(0);
        }

        // Game
        Random random = new Random();
        ArrayList<String> choices = new ArrayList<>(Arrays.asList("rock", "paper", "scissors"));
        String comChoice = choices.get(random.nextInt(3));
        String userChoice;

        while (true) {
            userChoice = JOptionPane.showInputDialog(null, "User:");

            if (!choices.contains(userChoice)) {
                continue;
            }
            JOptionPane.showMessageDialog(null, "Computer: " + comChoice.toUpperCase(), "Computer's choice", 2);

            if (userChoice.equals(comChoice)) {
                JOptionPane.showMessageDialog(null, "Draw!", "Result", 3);
            } else if ((userChoice.equals("rock") && comChoice.equals("scissors"))
                    || (userChoice.equals("paper") && comChoice.equals("rock"))
                    || (userChoice.equals("scissors") && comChoice.equals("paper"))) {
                JOptionPane.showMessageDialog(null, "You won!", "Result", 1);
            } else {
                JOptionPane.showMessageDialog(null, "You loss!", "Result", 0);
            }

            break;
        }

    }

}
