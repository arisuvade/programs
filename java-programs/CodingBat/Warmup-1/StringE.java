package Java.codingbat.warmup1;

public class StringE {

    public static void main(String[] args) {

        boolean test1 = stringE("Hello");
        boolean test2 = stringE("Heelele");

        System.out.println(test1);
        System.out.println(test2);

    }

    public static boolean stringE(String str) {
        int count = 0;

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == 'e') {
                count++;
            }
        }

        return (count > 0 && count <= 3);
    }

}
