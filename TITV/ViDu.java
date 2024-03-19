import java.util.Scanner;
public class ViDu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Nhap vao chuoi: ");
        String s = sc.nextLine();
        System.out.println("-------");

        //Ham length()
        System.out.println("Do dai cua chuoi: " + s.length());
        int doDai = s.length();
        //Ham charAt() => Lay ra vi tri cua 1 ky tu bat ky
        for (int i = 0; i < doDai; i++) {
            System.out.println("Vi tri " + i + " la: " + s.charAt(i));
        }

        //Ham getChars (vi tri bat dau, vi tri ket thuc, mang luu du lieu, vi tri bat dau luu mang)
        char[] arrChar = new char[100];
        s.getChars(2, 6, arrChar, 0);
        for (int i = 0; i < arrChar.length; i++) {
            System.out.println("Gia tri cua mang tai " + i + " la: " + arrChar[i]);
        }
        //Ham getByte => co 3 cach, lay ra gia tri cua cac ky tu thanh mot manng
        byte[] arrBytes = s.getBytes();
        for (byte b : arrBytes) {
            System.out.println(b);
        }
        sc.close();
    }
}
