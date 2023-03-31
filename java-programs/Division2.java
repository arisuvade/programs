package Exercises;

import java.util.Scanner;

public class Division2 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int a;
		int b;

		while (true) {
			try {
				System.out.print("Dividend: ");
				a = scanner.nextInt();
				System.out.print("Divisor: ");
				b = scanner.nextInt();
				break;
			} catch (Exception e) {
				System.out.println("Not a number");
				scanner.nextLine();
				continue;
			}
		}

		System.out.println("Quotient: " + ((double) a / b));

		scanner.close();

	}

}
