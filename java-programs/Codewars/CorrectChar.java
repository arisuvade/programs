package Codewars;

public class CorrectChar {

	public static void main(String[] args) {

		String test1 = correct("1F-RUDYARD K1PL1NG");
		String test2 = correct("R0BERT MERLE - THE DAY 0F THE D0LPH1N");

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String correct(String string) {
		return string.replace("5", "S").replace("0", "O").replace("1", "I");
	}

}
