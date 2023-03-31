package Exercises;

import java.util.Scanner;

public class Addition2 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int a;
		int b;

		while (true) {
			try {
				System.out.print("Addend: ");
				a = scanner.nextInt();
				System.out.print("Addend: ");
				b = scanner.nextInt();
				break;
			} catch (Exception e) {
				System.out.println("Not a number");
				scanner.nextLine();
				continue;
			}
		}

		System.out.println("Sum: " + (a + b));

		scanner.close();

	}

}
