class Employee{
    Employee(){
        System.out.println("Constructor is special method");
    }
    public static void main(String[] args) {
        new Employee();
        new Employee();
    }
}