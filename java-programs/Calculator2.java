package Exercises;

import java.util.Scanner;

public class Calculator2 {

	public static void main(String[] args) {

		String op;
		int x;
		int y;

		Scanner scanner = new Scanner(System.in);

		System.out.print("Operation: ");
		op = scanner.nextLine();

		switch (op.toLowerCase()) {

		case "addition":
			System.out.print("Addend: ");
			x = scanner.nextInt();
			System.out.print("Addend: ");
			y = scanner.nextInt();
			System.out.println("Sum: " + (x + y));
			break;

		case "subtraction":
			System.out.print("Minuend: ");
			x = scanner.nextInt();
			System.out.print("Subtrahend: ");
			y = scanner.nextInt();
			System.out.println("Difference: " + (x - y));
			break;

		case "multiplication":
			System.out.print("Multiplicand: ");
			x = scanner.nextInt();
			System.out.print("Multiplier: ");
			y = scanner.nextInt();
			System.out.println("Product: " + (x * y));
			break;

		case "division":
			System.out.print("Dividend: ");
			x = scanner.nextInt();
			System.out.print("Divisor: ");
			y = scanner.nextInt();
			System.out.println("Quotient: " + (x / y));
			break;

		default:
			System.out.println("Invalid operation");
		}

		scanner.close();

	}

}
