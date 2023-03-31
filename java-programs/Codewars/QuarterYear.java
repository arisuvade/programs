package Codewars;

public class QuarterYear {

	public static void main(String[] args) {

		int test1 = quarterOf(3);
		int test2 = quarterOf(11);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int quarterOf(int month) {

		if (month == 1 || month == 2 || month == 3) {
			return 1;
		} else if (month == 4 || month == 5 || month == 6) {
			return 2;
		} else if (month == 7 || month == 8 || month == 9) {
			return 3;
		} else {
			return 4;
		}

	}

}
