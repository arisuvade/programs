package codingbat;

public class Front22 {

	public static void main(String[] args) {

		String test1 = front22("a");
		String test2 = front22("Hello");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String front22(String str) {
		return (str.length() >= 2) ? str.substring(0, 2) + str + str.substring(0, 2) : str.repeat(3);
	}

}
