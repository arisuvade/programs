package codingbat;

public class DelDel {

	public static void main(String[] args) {

		String test1 = delDel("ad");
		String test2 = delDel("adelabc");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String delDel(String str) {
		return ((str.length() >= 4) && (str.substring(1, 4).equals("del"))) ? str.substring(0, 1) + str.substring(4)
				: str;
	}

}
