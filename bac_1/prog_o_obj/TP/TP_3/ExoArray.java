package TP.TP_3;

public class ExoArray {
	public static void main(String[] args) {
		int[] puissancesDeDeux = PuissancesDeDeux(20);
		int[] nombresImpairs = ImpairsDecroissants(20);
		int[] nombresAlternes = Nombre1ii(20);
		System.out.println(Sum(nombresImpairs));
		System.out.println(Average(nombresImpairs));

		Display(puissancesDeDeux);
		Display(nombresImpairs);
		Display(nombresAlternes);
		Display(ZipSum(nombresImpairs, nombresAlternes));
		System.out.println(Ordered(nombresImpairs));
		System.out.println(Ordered(puissancesDeDeux));
		System.out.println(Max(nombresAlternes));
		Display(ZipAverage(nombresImpairs, nombresAlternes));
	}

	public static int[] PuissancesDeDeux(int n) {
		int[] tableau = new int[n];

		for (int i = 0; i < n; i++) {
			tableau[i] = 1 << i;
		}
		return tableau;
	}

	public static int[] ImpairsDecroissants(int n) {
		int[] tableau = new int[n];
		int max_num = n * 2 - 1;

		for (int i = 0; i < n; i++, max_num -= 2) {
			tableau[i] = max_num;
		}
		return tableau;
	}

	public static int[] Nombre1ii(int n) {
		int[] tableau = new int[n];

		for (int i = 0; i < n; i++) {
			if (i % 2 == 0) {
				tableau[i] = i;
			} else {
				tableau[i] = -i;
			}
		}
		return tableau;
	}

	public static void Display(int[] tableau) {
		for (int i = 0; i < tableau.length; i++) {
			System.out.print(tableau[i] + " ");
		}
		System.out.println();
	}
	
	public static void Display(String[] tableau) {
		for (int i = 0; i < tableau.length; i++) {
			System.out.print(tableau[i] + " ");
		}
		System.out.println();
	}

	public static int Sum(int[] tableau) {
		int result = 0;
		
		for (int i = 0; i < tableau.length; i++) {
			result += tableau[i];
		}
		return result;
	}

	public static int Average(int[] tableau) {
		int length = tableau.length;
		return Sum(tableau) / length; 
	}
	
	public static int[] ZipSum(int[] t1, int[] t2) {
		if (t1.length != t2.length) return null;
		int length = t1.length;
		int[] tResult = new int[length];

		for (int i = 0; i < length; i++) {
			tResult[i] = t1[i] + t2[i];
		}
		return tResult;
	}
	
	public static int[] ZipAverage(int[] t1, int[] t2) {
		if (t1.length != t2.length) return null;
		int length = t1.length;
		int[] tResult = new int[length];

		for (int i = 0; i < length; i++) {
			tResult[i] = (t1[i] + t2[i]) / 2;
		}
		return tResult;
	}

	public static boolean Ordered(int[] tableau) {
		boolean hisCroissant = true;
		boolean hisDécroissant = true;
		
		for (int i = 0; i < tableau.length - 1; i++) {
			if (tableau[i] > tableau[i + 1]) {
				hisCroissant = false;
			}
		}
		for (int i = 0; i < tableau.length - 1; i++) {
			if (tableau[i] < tableau[i + 1]) {
				hisDécroissant = false;
			}
		}
		return hisCroissant || hisDécroissant;
	}

	public static int Max(int[] tableau) {
		int max = tableau[0];
		for (int i = 1; i < tableau.length; i++) {
			if (max < tableau[i]) {
				max = tableau[i];
			}
		}
		return max;
	}

	public static int[] StringToIntTable(String[] stringT) {
		int[] result = new int[stringT.length];
		for (int i = 0; i < stringT.length; i++) {
			result[i] = Integer.parseInt(stringT[i]);
		}
		return result;
	}
}
