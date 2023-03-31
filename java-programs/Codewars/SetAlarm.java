package Codewars;

public class SetAlarm {

	public static void main(String[] args) {

		boolean test1 = setAlarm(true, false);
		boolean test2 = setAlarm(true, true);

		System.out.println(test1);
		System.err.println(test2);

	}

	public static boolean setAlarm(boolean employed, boolean vacation) {
		return (employed == true && vacation == false) ? true : false;
	}
}
