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

        while (true) {
            System.out.println("Selecione o numero de opçoes (até 5):");
            String input = scan.nextLine();
            
            try {
                numOp = Integer.parseInt(input);
                
                if (numOp >= 1 && numOp <= 5) {
                    break; // Sai do loop se o número for válido
                } else {
                    System.out.println("Número inválido de opções!");
                }
            } catch (NumberFormatException e) {
                System.out.println("Digite apenas números!");
            }
        }

        for (int i = 0; i < numOp; i++) {
            System.out.println("Opção " + (i + 1) + ":");
            op[i] = scan.nextLine();
        }

        randomNum = rand.nextInt(numOp);

        System.out.println("O sistema escolheu a opção: " + op[randomNum]);
    }
}
