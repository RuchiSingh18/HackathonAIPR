// example.ts

// A simple function to add two numbers
export function add(a: number, b: number): number {
    return a + b;
}

// A function that returns a greeting message
export function greet(name: string): string {
    return `Hello, ${name}!`;
}

// A function that calculates the factorial of a number
export function factorial(n: number): number {
    if (n < 0) throw new Error("Negative input not allowed");

    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
