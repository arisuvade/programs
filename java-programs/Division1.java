package Exercises;

import java.util.Scanner;

public class Division1 {

	public static void main(String[] args) {

		int x;
		int y;

		Scanner scanner = new Scanner(System.in);

		System.out.print("Dividend: ");
		x = scanner.nextInt();
		System.out.print("Divisor: ");
		y = scanner.nextInt();

		System.out.println("Quotient: " + (x / y));

		scanner.close();

	}

}
