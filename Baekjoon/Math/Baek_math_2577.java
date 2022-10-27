package algorithm.demo.math;

import java.util.Scanner;

public class BaekJoon2577 {
    public static void main(String[] args) {

        int total;

        Scanner sc = new Scanner(System.in);
        int numA = sc.nextInt();
        int numB = sc.nextInt();
        int numC = sc.nextInt();

        total = numA*numB*numC;


        String answer = Integer.toString(total);




        for(int i = 0; i < 10 ; i++){
            int count=0;

            for (int j=0; j<answer.length(); j++){

                if((answer.charAt(j))-'0' == i){
                    count++;


                }

            }
            System.out.println(count);


        }

    }
}
