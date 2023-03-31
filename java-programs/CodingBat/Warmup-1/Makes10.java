package codingbat;

public class Makes10 {

	public static void main(String[] args) {

		boolean test1 = makes10(1, 9);
		boolean test2 = makes10(9, 9);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean makes10(int a, int b) {
		return ((a == 10 || b == 10) || a + b == 10);
	}

}
