public class Main {
    public static void main(String[] args) {
        System.out.println("Test dog: ");
        Dog d = new Dog();
        d.eat();
        d.makeSound();
        System.out.println("Test cat: ");
        Cat c = new Cat();
        c.eat();
        c.makeSound();
        System.out.println("Test bird: ");
        Bird b = new Bird();
        b.eat();
        b.makeSound();
    }
}
