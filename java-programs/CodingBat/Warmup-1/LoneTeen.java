package codingbat;

public class LoneTeen {

	public static void main(String[] args) {

		boolean test1 = loneTeen(13, 99);
		boolean test2 = loneTeen(13, 13);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean loneTeen(int a, int b) {
		return (((a >= 13 && a <= 19) && (b < 13 || b > 19)) || ((a < 13 || a > 19) && (b >= 13 && b <= 19)));
	}

}
