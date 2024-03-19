import java.util.Scanner;

public class ktraSNT {
    public static boolean isPrime(int n){
        //so nguyen < 2 thi khong phai so nguyen to
        if(n < 2){
            return false;
        }
        //check so nguyen to khi n >= 2
        for (int i = 2; i <= n/2; i++) {
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap n: ");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            if(isPrime(i)){
                System.out.print(i + " ");
            }
        }
        sc.close();
    }
}
