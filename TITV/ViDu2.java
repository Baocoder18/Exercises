public class ViDu2 {
    public static void main(String[] args) {
        String s1 = "baocoder";
        String s2 = "baocoder";
        String s3 = "BaoCoder";

        //Ham equals()
        System.out.println("s1 equals s2: " + s1.equals(s2));
        System.out.println("s1 equals s3: " + s1.equals(s3));

        //Ham euqalsIgnoreCase
        System.out.println("s1 equalsIgnoreCase s2: " + s1.equalsIgnoreCase(s2));
        System.out.println("s1 equalsIgnoreCase s3: " + s1.equalsIgnoreCase(s3));

        //Ham compareTo => So sanh
        String sv1 = "Nguyen Van A";
        String sv2 = "Nguyen Van B";
        String sv3 = "Nguyen Van C";
        String sv4 = "Nguyen Van";
        System.out.println("sv1 compare to sv2: " + sv1.compareTo(sv2));
        System.out.println("sv1 compare to sv3: " + sv1.compareTo(sv3));
        System.out.println("sv1 compare to sv4: " + sv1.compareTo(sv4));

        //Ham compareToIgnoreCase => Tuong tu ham compareTo, khong phan biet chu hoa hay chu thuong
    }
}
