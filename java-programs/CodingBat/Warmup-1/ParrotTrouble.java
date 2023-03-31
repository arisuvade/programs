package codingbat;

public class ParrotTrouble {

	public static void main(String[] args) {

		boolean test1 = parrotTrouble(true, 6);
		boolean test2 = parrotTrouble(false, 23);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean parrotTrouble(boolean talking, int hour) {
		return ((talking == true) && (hour < 7 || hour > 20));
	}

}
