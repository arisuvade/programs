package Java.codingbat.warmup1;

public class LastDigit {

    public static void main(String[] args) {

        boolean test1 = lastDigit(7, 17);
        boolean test2 = lastDigit(3, 14);

        System.out.println(test1);
        System.out.println(test2);

    }

    public static boolean lastDigit(int a, int b) {
        return ((a % 10) == (b % 10));
    }

}
