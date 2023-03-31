package codingbat;

public class StartOz {

	public static void main(String[] args) {

		String test1 = startOz("oo");
		String test2 = startOz("bzoo");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String startOz(String str) {
		return ((str.length() > 0) && (str.substring(0, 2).equals("oz"))) ? "oz"
				: ((str.length() > 0) && (str.charAt(0) == 'o')) ? "o"
						: ((str.length() > 2) && (str.charAt(1) == 'z')) ? "z" : (str.length() >= 1) ? "" : str;
	}
}
