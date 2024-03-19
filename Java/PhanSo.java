public class PhanSo {
    private int tuSo;
    private int mauSo;

    public PhanSo(int tuSo, int mauSo){
        this.tuSo = tuSo;
        this.mauSo = mauSo;
    }
    public PhanSo(){
    }
    public static void main(String[] args) {
        PhanSo ps1 = new PhanSo();
        PhanSo ps2 = new PhanSo(3, 4);
        System.out.println(ps1.tuSo + "/" + ps1.mauSo);
        System.out.println(ps2.tuSo + "/" + ps2.mauSo);
    }
}
