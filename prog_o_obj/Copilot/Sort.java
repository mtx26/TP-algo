package Copilot;
import java.util.*;

public class Sort {

    // Tri "built-in" en Java
    public static void pythonSort(ArrayList<Integer> t) {
        Collections.sort(t);
    }

    // Tri par insertion (in-place)
    public static void insertionSort(ArrayList<Integer> t) {
        int n = t.size();
        for (int i = 1; i < n; i++) {
            int clef = t.get(i);
            int j = i - 1;
            while (j >= 0 && t.get(j) > clef) {
                t.set(j + 1, t.get(j));
                j = j - 1;
            }
            t.set(j + 1, clef);
        }
    }

    // Tri par sélection (in-place)
    public static void selectionSort(ArrayList<Integer> t) {
        int n = t.size();
        for (int i = 0; i < n - 1; i++) {
            int small = i;
            for (int j = i + 1; j < n; j++) {
                if (t.get(j) < t.get(small)) {
                    small = j;
                }
            }
            int tmp = t.get(i);
            t.set(i, t.get(small));
            t.set(small, tmp);
        }
    }

    // Merge sort fonctionnel (retourne une nouvelle liste)
    public static ArrayList<Integer> mergeSort(ArrayList<Integer> t) {
        int n = t.size();
        if (n <= 1) {
            return new ArrayList<>(t);
        }
        int mid = n / 2;
        ArrayList<Integer> left = new ArrayList<>(t.subList(0, mid));
        ArrayList<Integer> right = new ArrayList<>(t.subList(mid, n));
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }

    private static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b) {
        ArrayList<Integer> res = new ArrayList<>(a.size() + b.size());
        int i = 0, j = 0;
        while (i < a.size() && j < b.size()) {
            if (a.get(i) <= b.get(j)) {
                res.add(a.get(i));
                i++;
            } else {
                res.add(b.get(j));
                j++;
            }
        }
        while (i < a.size()) { res.add(a.get(i)); i++; }
        while (j < b.size()) { res.add(b.get(j)); j++; }
        return res;
    }

    // Recherche dichotomique (binaire). Retourne l'indice ou null si absent.
    public static Integer dichoSearch(ArrayList<Integer> t, int x) {
        int start = 0;
        int end = t.size() - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int val = t.get(mid);
            if (val == x) return mid;
            if (x < val) end = mid - 1;
            else start = mid + 1;
        }
        return null;
    }

    // Crée une copie profonde d'une liste d'entiers
    private static ArrayList<Integer> copyList(ArrayList<Integer> t) {
        return new ArrayList<>(t);
    }

    // Mesure et affiche les temps pour des listes de taille n
    public static void test(int n) {
        ArrayList<Integer> t1 = new ArrayList<>(n);
        for (int i = 0; i < n; i++) t1.add(i);
        ArrayList<Integer> t2 = new ArrayList<>(n);
        for (int i = n; i > 0; i--) t2.add(i);
        ArrayList<Integer> t3 = new ArrayList<>(n);
        Random rand = new Random();
        for (int i = 0; i < n; i++) t3.add(rand.nextInt(n + 1));

        double s1, i1, m1, s2, i2, m2, s3, i3, m3;

        long start, end;

        // t1: croissante
        ArrayList<Integer> tmp = copyList(t1);
        start = System.nanoTime(); selectionSort(tmp); end = System.nanoTime(); s1 = (end - start) / 1_000_000.0;

        tmp = copyList(t1);
        start = System.nanoTime(); insertionSort(tmp); end = System.nanoTime(); i1 = (end - start) / 1_000_000.0;

        tmp = copyList(t1);
        start = System.nanoTime(); ArrayList<Integer> r = mergeSort(tmp); end = System.nanoTime(); m1 = (end - start) / 1_000_000.0;

        // t2: décroissante
        tmp = copyList(t2);
        start = System.nanoTime(); selectionSort(tmp); end = System.nanoTime(); s2 = (end - start) / 1_000_000.0;

        tmp = copyList(t2);
        start = System.nanoTime(); insertionSort(tmp); end = System.nanoTime(); i2 = (end - start) / 1_000_000.0;

        tmp = copyList(t2);
        start = System.nanoTime(); r = mergeSort(tmp); end = System.nanoTime(); m2 = (end - start) / 1_000_000.0;

        // t3: aléatoire
        tmp = copyList(t3);
        start = System.nanoTime(); selectionSort(tmp); end = System.nanoTime(); s3 = (end - start) / 1_000_000.0;

        tmp = copyList(t3);
        start = System.nanoTime(); insertionSort(tmp); end = System.nanoTime(); i3 = (end - start) / 1_000_000.0;

        tmp = copyList(t3);
        start = System.nanoTime(); r = mergeSort(tmp); end = System.nanoTime(); m3 = (end - start) / 1_000_000.0;

        System.out.printf("%7d %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f\n",
                n, s1, i1, m1, s2, i2, m2, s3, i3, m3);
    }

    public static void main(String[] args) {
        System.out.println("n : taille des listes");
        System.out.println("t1 : temps pour des listes triées croissantes");
        System.out.println("t2 : temps pour des listes triées décroissantes");
        System.out.println("t3 : temps pour des listes remplies aléatoirement");
        System.out.println("Temps en millisecondes");
        System.out.println("      n "
                + "t1: sel "
                + "    ins "
                + "    mer "
                + "t2: sel "
                + "    ins "
                + "    mer "
                + "t3: sel "
                + "    ins "
                + "    mer");
        for (int i = 100; i <= 900; i += 100) {
            test(i);
        }
    }
}
