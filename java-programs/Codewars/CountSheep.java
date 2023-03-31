package Codewars;

public class CountSheep {

	public static void main(String[] args) {

		String test1 = countingSheep(1);
		String test2 = countingSheep(3);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static String countingSheep(int num) {

		String sheepCounting = "";
		for (int i = 1; i <= num; i++) {
			sheepCounting += i + " sheep...";
		}
		return sheepCounting;

	}

}
