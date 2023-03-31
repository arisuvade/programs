package Codewars;

public class OppositesAttract {

	public static void main(String[] args) {

		boolean test1 = isLove(1, 4);
		boolean test2 = isLove(2, 2);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean isLove(final int flower1, final int flower2) {

		if ((flower1 % 2 == 1 && flower2 % 2 == 0) || (flower1 % 2 == 0 && flower2 % 2 == 1)) {
			return true;
		} else {
			return false;
		}

	}

}
