package codingbat;

public class Diff21 {

	public static void main(String[] args) {

		int test1 = diff21(21);
		int test2 = diff21(25);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int diff21(int n) {
		return n <= 21 ? 21 - n : (n - 21) * 2;
	}
}
