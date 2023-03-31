package Codewars;

public class SwitchItUp {

	public static void main(String[] args) {

		String test1 = switchItUp(1);
		String test2 = switchItUp(3);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String switchItUp(int number) {

		switch (number) {
		case 0:
			return "Zero";
		case 1:
			return "One";
		case 2:
			return "Two";
		case 3:
			return "Three";
		case 4:
			return "Four";
		case 5:
			return "Five";
		case 6:
			return "Six";
		case 7:
			return "Seven";
		case 8:
			return "Eight";
		case 9:
			return "Nine";
		default:
			return "";
		}

	}

}
