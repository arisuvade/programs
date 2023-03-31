package codingbat;

public class StartHi {

	public static void main(String[] args) {

		boolean test1 = startHi("hi");
		boolean test2 = startHi("hello hi");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean startHi(String str) {
		return (str.startsWith("hi"));
	}

}
