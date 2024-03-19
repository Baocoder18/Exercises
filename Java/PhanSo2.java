public class PhanSo2 {
    private int tuSo;
    private int mauSo;

    public PhanSo2(){
    }
    public PhanSo2(int tuSo, int mauSo){
        this.tuSo = tuSo;
        this.mauSo = mauSo;
    }
    public int getTuSo(){
        return this.tuSo;
    }
    public void setTuSo(int tuSo){
        this.tuSo = tuSo;
    }
    public int getMauSo(){
        return this.mauSo;
    }
    public void setMauSo(int mauSo){
        if(mauSo != 0){
            this.mauSo = mauSo;
        }
        
    }
}
