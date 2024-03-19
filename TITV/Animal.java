public class Animal {
    //Overriding: Ghi de phuong thuc
    private String name;
    public Animal(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public void setName(String name){
        this.name = name;
    }
    public void eat(){
        System.out.println("Mam mam.....");
    }
    public void makeSound(){
        System.out.println(".....");
    }
    public void sleep(){
        System.out.println("Zzzzzz");
    }
}
