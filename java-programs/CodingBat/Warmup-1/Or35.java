package codingbat;

public class Or35 {

	public static void main(String[] args) {

		boolean test1 = or35(10);
		boolean test2 = or35(8);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean or35(int n) {
		return (n % 3 == 0 || n % 5 == 0);
	}

}
