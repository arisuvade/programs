package codingbat;

public class MonkeyTrouble {

	public static void main(String[] args) {

		boolean test1 = monkeyTrouble(true, true);
		boolean test2 = monkeyTrouble(true, false);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
		return (aSmile == bSmile);
	}

}
