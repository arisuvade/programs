package codingbat;

public class NearHundred {

	public static void main(String[] args) {

		boolean test1 = nearHundred(90);
		boolean test2 = nearHundred(89);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean nearHundred(int n) {
		return ((Math.abs(100 - n) <= 10) || (Math.abs(200 - n) <= 10));
	}

}
