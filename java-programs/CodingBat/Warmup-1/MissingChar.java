package codingbat;

public class MissingChar {

	public static void main(String[] args) {

		String test1 = missingChar("kitten", 0);
		String test2 = missingChar("kitten", 4);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String missingChar(String str, int n) {
		return str.substring(0, n) + str.substring(n + 1);
	}

}
