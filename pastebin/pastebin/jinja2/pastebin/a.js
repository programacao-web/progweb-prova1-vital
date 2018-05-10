class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    is_adult() {
        return self.age >= 18
    }
}

people = [new Person('Joao', 21), new Person('Maria', 20), new Person('Zé', 8)]

adults = people.map((x)=>{
    if(x.is_adult()){
        return x;
    }
});

let sum = 0;
people.forEach(x => sum = sum + x.age);
mean_age = sum / adults.length;
