package TP.TP_3;

import java.util.Arrays;

public class ExoArray {
	public static void main(String[] args) {
		int[] puissancesDeDeux = creerPuissancesDeDeux(20);
		int[] nombresImpairs = creerImpairsDecroissants(20);

		System.out.println("Puissances de 2 : " + Arrays.toString(puissancesDeDeux));
		System.out.println("Nombres impairs decroissants : " + Arrays.toString(nombresImpairs));
	}

	public static int[] creerPuissancesDeDeux(int taille) {
		int[] tableau = new int[taille];

		for (int index = 0; index < tableau.length; index++) {
			tableau[index] = 1 << index;
		}

		return tableau;
	}

	public static int[] creerImpairsDecroissants(int taille) {
		int[] tableau = new int[taille];
		int impair = taille * 2 - 1;

		for (int index = 0; index < tableau.length; index++) {
			tableau[index] = impair;
			impair -= 2;
		}

		return tableau;
	}
}
