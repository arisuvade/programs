package Codewars;

public class EnoughSpace {

	public static void main(String[] args) {

		int test1 = enough(10, 5, 5);
		int test2 = enough(100, 60, 50);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int enough(int cap, int on, int wait) {

		if (cap >= (on + wait)) {
			return 0;
		} else {
			return (on + wait) - cap;
		}

	}

}
