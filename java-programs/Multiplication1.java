package Exercises;

import java.util.Scanner;

public class Multiplication1 {

	public static void main(String[] args) {

		int x;
		int y;

		Scanner scanner = new Scanner(System.in);

		System.out.print("Multiplicand: ");
		x = scanner.nextInt();
		System.out.print("Multiplier: ");
		y = scanner.nextInt();

		System.out.println("Product: " + (x * y));

		scanner.close();

	}

}
