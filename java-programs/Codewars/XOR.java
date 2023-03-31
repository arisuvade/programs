package Codewars;

public class XOR {

	public static void main(String[] args) {

		boolean test1 = xor(false, false);
		boolean test2 = xor(true, false);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean xor(boolean a, boolean b) {
		return !a == b;
	}

}
