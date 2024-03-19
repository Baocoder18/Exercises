public class Main {
    public static void main(String[] args) {
        PhanSo2 ps1 = new PhanSo2();
        PhanSo2 ps2 = new PhanSo2(3,4);
        System.out.println(ps1.getTuSo() + "/" + ps1.getMauSo());
        System.out.println(ps2.getTuSo() + "/" + ps2.getMauSo());

        ps1.setTuSo(5);
        ps1.setMauSo(2);
        ps2.setTuSo(4);
        ps2.setMauSo(6);
        System.out.println(ps1.getTuSo() + "/" + ps1.getMauSo());
        System.out.println(ps2.getTuSo() + "/" + ps2.getMauSo());
    }
}
