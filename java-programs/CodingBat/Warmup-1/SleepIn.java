package codingbat;

public class SleepIn {

	public static void main(String[] args) {

		boolean test1 = sleepIn(false, false);
		boolean test2 = sleepIn(true, false);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static boolean sleepIn(boolean weekday, boolean vacation) {
		return (weekday == false && vacation == false);
	}

}
