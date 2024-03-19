public class Dog extends Animal {
    public Dog(){
        super("Dog");
    }
    @Override
    public void eat(){
        System.out.println("Toi an xuong");
    }
    public void makeSound(){
        System.out.println("Gau gau");
    }
}
