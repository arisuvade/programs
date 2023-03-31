package Codewars;

public class Goals {

	public static void main(String[] args) {

		int test1 = goals(0, 0, 0);
		int test2 = goals(43, 10, 5);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static int goals(int laLigaGoals, int copaDelReyGoals, int championsLeagueGoals) {
		return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
	}

}
