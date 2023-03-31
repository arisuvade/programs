package Java.codingbat.warmup1;

public class EndUp {

    public static void main(String[] args) {

        String test1 = endUp("hi");
        String test2 = endUp("hello");

        System.out.println(test1);
        System.out.println(test2);

    }

    public static String endUp(String str) {
        if (str.length() <= 3) {
            return str.toUpperCase();
        } else {
            String lowerStr = str.substring(0, str.length() - 3);
            return lowerStr + str.substring(str.length() - 3).toUpperCase();
        }
    }

}
