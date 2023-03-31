package Exercises;

import java.util.Scanner;

public class Multiplication2 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int a;
		int b;

		while (true) {
			try {
				System.out.print("Multiplicand: ");
				a = scanner.nextInt();
				System.out.print("Multiplier: ");
				b = scanner.nextInt();
				break;
			} catch (Exception e) {
				System.out.println("Not a number");
				scanner.nextLine();
				continue;
			}
		}

		System.out.println("Product: " + (a * b));

		scanner.close();

	}

}
