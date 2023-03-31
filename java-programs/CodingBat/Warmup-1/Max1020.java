package Java.codingbat.warmup1;

public class Max1020 {

	public static void main(String[] args) {

		int test1 = max1020(11, 19);
		int test2 = max1020(11, 9);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int max1020(int a, int b) {
		return (a >= 10 && b >= 10) ? Math.max(a, b) : 0;
	}

}
