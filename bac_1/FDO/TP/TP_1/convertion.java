package bac_1.FDO.TP.TP_1;

public class convertion {
    private static final String[] DIGITS = {
        "0","1","2","3","4","5","6","7","8","9",
        "A","B","C","D","E","F"
    };

    public static String tohexa(int d) {
        return toBase(d, 16);
    }

    public static String toBase(int value, int base) {
        String result = "";
        int quotien = value;

        while (quotien > 0) {
            int reste = quotien % base;
            result = DIGITS[reste] + result;
            quotien = quotien / base;
        }

        return result;
    }

    public static void main(String[] args) {
        int valeur = 51966;
        System.out.println("Décimal 123 en hexadécimal = " + tohexa(valeur));
    }
}
