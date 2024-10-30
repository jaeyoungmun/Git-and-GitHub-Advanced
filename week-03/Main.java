import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Main instance = new Main();
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        instance.solve(N);
        sc.close();
    }

    public void solve(int N) {
        printPyramid(N);
        printInvertedPyramid(N);
    }

    public void printPyramid(int N) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Not implemented yet");
    }

    public void printInvertedPyramid(int N) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Not implemented yet");
    }
}