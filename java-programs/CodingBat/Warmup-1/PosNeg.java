package codingbat;

public class PosNeg {

	public static void main(String[] args) {

		boolean test1 = posNeg(-1, -1, true);
		boolean test2 = posNeg(1, 1, false);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean posNeg(int a, int b, boolean negative) {
		return ((((a < 0 && b > 0) || (a > 0 && b < 0)) && negative == false) || (a < 0 && b < 0) && negative == true);
	}
}
