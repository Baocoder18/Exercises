public class Test {
    public static void main(String[] args) {
        MyMath mm = new MyMath();
        System.out.println("Min(2,3): " + mm.timMin(2, 3));
        System.out.println("Min(5.5, 6.0): " + mm.timMin(5.5, 6.0));
        double arr[] = new double[] {1, 2, 3, 4, 5};
        System.out.println("Tinh tong arr: " + mm.tinhTong(arr));
    }
}
