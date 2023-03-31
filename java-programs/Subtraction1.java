package Exercises;

import java.util.Scanner;

public class Subtraction1 {

	public static void main(String[] args) {

		int x;
		int y;

		Scanner scanner = new Scanner(System.in);

		System.out.print("Minuend: ");
		x = scanner.nextInt();
		System.out.print("Subtrahend: ");
		y = scanner.nextInt();

		System.out.println("Difference: " + (x - y));

		scanner.close();

	}

}