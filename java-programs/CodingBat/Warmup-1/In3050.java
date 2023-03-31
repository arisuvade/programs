package codingbat;

public class In3050 {

	public static void main(String[] args) {

		boolean test1 = in3050(30, 31);
		boolean test2 = in3050(30, 41);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean in3050(int a, int b) {
		return (((a >= 30 && a <= 40) && (b >= 30 && b <= 40)) || ((a >= 40 && a <= 50) && (b >= 40 && b <= 50)));
	}

}
