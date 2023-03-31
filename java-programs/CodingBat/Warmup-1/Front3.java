package codingbat;

public class Front3 {

	public static void main(String[] args) {

		String test1 = front3("Java");
		String test2 = front3("Chocolate");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String front3(String str) {
		return str.substring(0, 3).repeat(3);
	}
}
