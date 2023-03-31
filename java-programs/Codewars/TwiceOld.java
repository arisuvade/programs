package Codewars;

public class TwiceOld {

	public static void main(String[] args) {

		int test1 = TwiceAsOld(30, 0);
		int test2 = TwiceAsOld(45, 30);

		System.out.println(test1);
		System.err.println(test2);
	}

	public static int TwiceAsOld(int dadYears, int sonYears) {
		return Math.abs(dadYears - (sonYears * 2));
	}

}
