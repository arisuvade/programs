package codingbat;

public class IcyHot {

	public static void main(String[] args) {

		boolean test1 = icyHot(-1, 120);
		boolean test2 = icyHot(2, 120);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean icyHot(int temp1, int temp2) {
		return ((temp1 > 100 && temp2 < 0) || (temp1 < 0 && temp2 > 100));
	}

}
