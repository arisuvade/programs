package codingbat;

public class In1020 {

	public static void main(String[] args) {

		boolean test1 = in1020(20, 10);
		boolean test2 = in1020(2, 120);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean in1020(int a, int b) {
		return ((a >= 10 && a <= 20) || (b >= 10 && b <= 20));
	}

}
