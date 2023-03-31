package Exercises;

import java.util.Scanner;

public class Calculator1 {

	public static void main(String[] args) {

		String op;
		int x;
		int y;

		Scanner scanner = new Scanner(System.in);

		System.out.print("Operation: ");
		op = scanner.nextLine();

		if (op.toLowerCase().equals("addition")) {

			System.out.print("Addend: ");
			x = scanner.nextInt();
			System.out.print("Addend: ");
			y = scanner.nextInt();
			System.out.println("Sum: " + (x + y));

		} else if (op.toLowerCase().equals("subtraction")) {

			System.out.print("Minuend: ");
			x = scanner.nextInt();
			System.out.print("Subtrahend: ");
			y = scanner.nextInt();
			System.out.println("Difference: " + (x - y));

		} else if (op.toLowerCase().equals("multiplication")) {

			System.out.print("Multiplicand: ");
			x = scanner.nextInt();
			System.out.print("Multiplier: ");
			y = scanner.nextInt();
			System.out.println("Product: " + (x * y));

		} else if (op.toLowerCase().equals("division")) {

			System.out.print("Dividend: ");
			x = scanner.nextInt();
			System.out.print("Divisor: ");
			y = scanner.nextInt();
			System.out.println("Quotient: " + (x / y));

		} else {
			System.out.println("Invalid operation");
		}

		scanner.close();

	}

}
