package codingbat;

public class NotString {

	public static void main(String[] args) {

		String test1 = notString("x");
		String test2 = notString("not bad");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String notString(String str) {
		return (str.startsWith("not")) ? str : "not " + str;
	}

}
