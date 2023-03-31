package Codewars;

public class SayHello {

	public static void main(String[] args) {

		String test1 = sayHello("Aries");
		String test2 = sayHello("Dave");

		System.out.println(test1);
		System.err.println(test2);

	}

	public static String sayHello(String name) {
		return "Hello, " + name;
	}

}
