
public class MatrixMultiplication {
    public static double[][] multiply(double[][] A, double[][] B) {
        if (A[0].length != B.length)
            return null;

        double[][] C = new double[A.length][B[0].length];

        for (int i = 0; i < A.length; i++)
            for(int j = 0; j < B[0].length; j++) {
                double sum = 0;
                for (int k = 0; k < A[0].length; k++)
                    sum += A[i][k]*B[k][j];
                C[i][j] = sum;
            }
        return C;
    }

    public static void main(String[] args) {
        double[][] A = { {1, 2}, {3, 4} };
        double[][] B = { {5, 6}, {7, 8} };
        double[][] C = multiply(A, B);
        if (C == null) {
            System.out.println("Multiplication impossible : dimensions incompatibles.");
            return;
        }
        for (double[] row : C) {
            for (double val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}