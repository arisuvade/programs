package codingbat;

public class SumDouble {

	public static void main(String[] args) {

		int test1 = sumDouble(1, 2);
		int test2 = sumDouble(2, 2);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int sumDouble(int a, int b) {
		return a == b ? (a + b) * 2 : a + b;
	}

}
