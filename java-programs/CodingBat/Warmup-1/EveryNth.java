package Java.codingbat.warmup1;

public class EveryNth {

    public static void main(String[] args) {

        String test1 = everyNth("Miracle", 2);
        String test2 = everyNth("abcedefg", 3);

        System.out.println(test1);
        System.out.println(test2);

    }

    public static String everyNth(String str, int n) {
        String result = "";

        for (int i = 0; i < str.length(); i = i + n) {
            result = result + str.charAt(i);
        }
        return result;
    }

}
