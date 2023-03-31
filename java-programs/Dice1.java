package Exercises;

import java.util.Random;

public class Dice1 {

	public static void main(String[] args) {

		Random random = new Random();

		int d1 = random.nextInt(6);
		int d2 = random.nextInt(6);

		System.out.println(d1 + 1);
		System.out.println(d2 + 1);

	}

}
