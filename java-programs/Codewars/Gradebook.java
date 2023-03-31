package Codewars;

public class Gradebook {

	public static void main(String[] args) {

		char test1 = getGrade(95, 90, 93);
		char test2 = getGrade(100, 70, 70);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static char getGrade(int s1, int s2, int s3) {

		int grade = (s1 + s2 + s3) / 3;

		if (grade >= 90)
			return 'A';
		else if (grade >= 80)
			return 'B';
		else if (grade >= 70)
			return 'C';
		else if (grade >= 60)
			return 'D';
		else
			return 'F';

	}

}
