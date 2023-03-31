package codingbat;

public class HasTeen {

	public static void main(String[] args) {

		boolean test1 = hasTeen(13, 20, 10);
		boolean test2 = hasTeen(20, 20, 20);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean hasTeen(int a, int b, int c) {
		return ((a >= 13 && a <= 19) || (b >= 13 && b <= 19) || (c >= 13 && c <= 19));
	}

}
