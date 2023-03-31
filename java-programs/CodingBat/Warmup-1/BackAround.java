package codingbat;

public class BackAround {

	public static void main(String[] args) {

		String test1 = backAround("cat");
		String test2 = backAround("Hello");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String backAround(String str) {
		return str.charAt(str.length() - 1) + str + str.charAt(str.length() - 1);
	}
}
