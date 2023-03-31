package codingbat;

public class FrontBack {

	public static void main(String[] args) {

		String test1 = frontBack("a");
		String test2 = frontBack("Chocolate");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String frontBack(String str) {
		return (str.length() >= 2)
				? (char) str.charAt(str.length() - 1) + str.substring(1, str.length() - 1) + (char) str.charAt(0)
				: str;
	}

}
