package codingbat;

public class MixStart {

	public static void main(String[] args) {

		boolean test1 = mixStart("pix snacks");
		boolean test2 = mixStart("piz snacks");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean mixStart(String str) {
		return (str.length() >= 3) ? (str.substring(1, 3).equals("ix")) : false;
	}

}
