package onboarding;

import java.util.List;

class Problem1 {
    public static int solution(List<Integer> pobi, List<Integer> crong) {

        int i;
        int maxResult=0;
        int answer = Integer.MAX_VALUE;


        if(pobi.get(0)%2==0 || pobi.get(1)%2!=0 || pobi.size()==1 || pobi.get(1)- pobi.get(0)!=1){
            answer=-1;
            return  answer;
        }

        if(crong.get(0)%2==0 || crong.get(1)%2!=0 || crong.size()==1 || crong.get(1)- crong.get(0)!=1){
            answer=-1;
            return  answer;
        }

        int resultMax = getResultMax(pobi);
        int resultMax1 = getResultMax(crong);


        return getAnswer(answer,resultMax,resultMax1);


    }


    public static int getResultMax(List<Integer> pobi) {
        int resultMax=0;
        int total=0;


        for(int i =0;i<2;i++){

            int num = pobi.get(i);
            int sum1=0;
            int sum2=1;

            while (num!=0){
                sum1+=num%10;
                sum2*=num%10;

                num /= 10;

            }

            total = Math.max(sum1,sum2);

            if(resultMax<total){
                resultMax=total;
            }


        }
        return resultMax;
    }

    public static int getAnswer(int answer, int resultMax, int resultMax1) {
        if(resultMax1 > resultMax){
            answer =2;
        }
        else if (resultMax1 < resultMax) {
            answer =1;
        }
        else if(resultMax1 == resultMax) {
            answer =0;
        }
        return answer;
    }



}
