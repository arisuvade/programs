package Exercises;

import java.util.Random;

public class Die1 {

	public static void main(String[] args) {

		Random random = new Random();

		int d = random.nextInt(6);

		System.out.println(d + 1);

	}

}
