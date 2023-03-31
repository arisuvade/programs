package Exercises;

import java.util.Scanner;

public class Addition1 {

	public static void main(String[] args) {

		int x;
		int y;

		Scanner scanner = new Scanner(System.in);

		System.out.print("Addend: ");
		x = scanner.nextInt();
		System.out.print("Addend: ");
		y = scanner.nextInt();

		System.out.println("Sum: " + (x + y));

		scanner.close();

	}

}
