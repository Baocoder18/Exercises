public abstract class Hinh {
    //Abstract class: lop truu tuong
    protected ToaDo toaDo;
    
    public Hinh(ToaDo toaDo){
        this.toaDo = toaDo;
    }
    public ToaDo getToaDo(){
        return this.toaDo;
    }
    public void setToaDo(ToaDo toaDo){
        this.toaDo = toaDo;
    }
    public abstract double tinhDienTich();
}
