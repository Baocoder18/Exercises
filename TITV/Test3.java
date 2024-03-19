public class Test3 {
    public static void main(String[] args) {
        System.out.println("Test cau a: ");
        MayTinhCasioFX500 mfx500 = new MayTinhCasioFX500();
        MayTinhVinaCal500 mvn500 = new MayTinhVinaCal500();
        System.out.println("5 + 3 = " + mfx500.cong(5, 3));
        System.out.println("4 * 3 = " + mfx500.nhan(4, 5));
        System.out.println("4 / 3 = " + mvn500.chia(4, 0));

        System.out.println("Test cau b: ");
        double[] arr = new double[] {5,4,3,2,1,0,6};
        double[] arr2 = new double[] {6,2,3,7,2,1};
        SapXepChen sxc = new SapXepChen();
        SapXepChon sxchon = new SapXepChon();

        sxc.sapXepTang(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        sxchon.sapXepGiam(arr2);
        for (int i = 0; i < arr2.length; i++) {
            System.out.print(arr2[i] + " ");
        }
    }
}
