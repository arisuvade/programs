package codingbat;

public class Close10 {

	public static void main(String[] args) {

		int test1 = close10(10, -10);
		int test2 = close10(13, 3);
		System.out.println(test1);
		System.out.println(test2);

	}

	public static int close10(int a, int b) {
		int adiff10 = Math.abs(a - 10);
		int bdiff10 = Math.abs(b - 10);
		int result = Math.min(adiff10, bdiff10);
		return (adiff10 == bdiff10) ? 0 : (adiff10 == result) ? a : b;
	}

}
