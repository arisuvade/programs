package codingbat;

public class IntMax {

	public static void main(String[] args) {

		int test1 = intMax(1, 2, 3);
		int test2 = intMax(6, 5, 4);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int intMax(int a, int b, int c) {
		return (Math.max(a, b)) > c ? Math.max(a, b) : c;
	}

}
