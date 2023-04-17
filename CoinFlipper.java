import java.util.Scanner;
import java.util.Random;

public class CoinFlipper {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        String[] op = new String[5];
        int numOp;
        int randomNum;

        System.out.println("O programa deve escolher aleatoriamente alguma opcao digitada por voce");
        System.out.println("Selecione o numero de opçoes(até 5):");
        numOp = scan.nextInt();
        scan.nextLine();

        if (numOp < 1 || numOp > 5) {
            System.out.println("Número inválido de opções!");
            return;
        }

        for (int i = 0; i < numOp; i++) {
            System.out.println("Opção " + (i + 1) + ":");
            op[i] = scan.nextLine();
        }

        randomNum = rand.nextInt(numOp);

        System.out.println("O sistema escolheu a opção: " + op[randomNum]);
    }
}