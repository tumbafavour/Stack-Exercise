------JAVA---------
package com.JavaProject;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        num number = new num();
        number.fibonacci(10);
//        int[] values = {0, 1};
//        System.out.println(javaArray(5));

    }
    public static String javaArray(int num){
        int values[] = new int[num];
        values[0] = 0;
        values[1] = 1;
        int i = 1;
        while(i < num - 1){
            i += 1;
            values[i] = values[i - 1] + values[i -2];
        }

        return Arrays.toString(values);
    }
    public static class num{
        // Factorial
        public void computeFactorial(int num){
            int factorial = num;
            int i = 0;

            while(num > (i + 1)){
                i += 1;
                factorial *= (num - i);
            }
            System.out.println(num + "!= " + factorial);
        }

        // Ackermann sequence
        public int ackermann(int m, int n){
            if(m == 0){
                return n + 1;
            }
            else if(m > 0 && n==0){
                return ackermann(m - 1, 1);
            }
            else if(m > 0 && n > 0){
                return ackermann(m-1, ackermann(m, n-1));
            }
            return 0;
        }

        // Fibonacci Sequence
        public void fibonacci(int num){
            if(num <= 0){
                int[] val ={};
                System.out.println(Arrays.toString(val));
            }
            else if(num == 1){
                int[] val = {0};
                System.out.println(Arrays.toString(val));
            }
            else if(num == 2){
                int[] val = {0, 1};
                System.out.println(Arrays.toString(val));
            }
            else{
                int values[] = new int[num];
                values[0] = 0;
                values[1] = 1;
                int i = 1;
                while(i < num - 1){
                    i += 1;
                    values[i] = values[i - 1] + values[i -2];
                }

                System.out.println(Arrays.toString(values));
            }
        }
    }
}



----------Python--------

# Factorial
def computeFactorial(num):
    factorial = num
    i = 0
    while(num > (i+1)):
        i += 1
        factorial *= (num - i)
    return factorial

# Factorial Input Function
def factorialApp():
    num = int(input('Enter the number for computing: '))
    print(f'{num}! = {computeFactorial(num)}')


# Ackermann Sequence
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Ackermann Input Function
def ackermanApp():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = ackermann(num1, num2)
    print(f"Ackermann({num1}, {num2}) =", result)

# Function Runner
def run(funtion):
    return funtion

# Fibonacci Sequence
def fibonacci(num):
    if(num <= 0):
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0,1]
    else:
        sequence = [0, 1]
        while len(sequence) < num:
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        return sequence

# Fibonacci Input Function
def fibonacciApp():
    length = int(input('Enter the number of values: '))
    print(fibonacci(length))

run(ackermanApp())

----------C--------

#include <stdio.h>
#include <stdlib.h>

// Factorial Function
int computeFactorial(int num){
    int factorial = num;
    int i = 0;
    while(num > (i + 1)){
        i += 1;
        factorial *= num - i;
    }
    return factorial;
}

// Ackermann Function
int ackermann(int m, int n){
    if(m == 0){
        return n + 1;
    }
    else if(m > 0 && n==0){
        return ackermann(m-1, 1);
    }
    else if(m > 0 && n > 0){
        return ackermann(m-1, ackermann(m, n-1));
    }
    return 0;
}

// Fibonacci Function
void fibonacci(int num){
    if(num <= 0){
        printf("{}");

    }
    else if(num == 1){
        printf("{ 0 }");
    }
    else if(num == 2){
        printf("{ 0, 1 }");
    }
    else{
        int values[num];
        values[0] = 0;
        values[1] = 1;
        int i = 1;
        while(i < num - 1){
            i += 1;
            values[i] = values[i - 1] + values[ i - 2];
        }
        printf("{ ");
        for(int j = 0; j < num; j++){
            printf("%d, ", values[j]);
        }
        printf("}");
    }
}

int main()
{
//    int number;
//    printf("Enter number to compute: ");
//    scanf("%d", &number);
//    printf("%d! = %d", number, computeFactorial(number));
    fibonacci(8);
    return 0;
}


--------C++--------

#include <iostream>

using namespace std;

// Factorial Function
int computeFactorial(int num){
    int factorial = num;
    int i = 0;
    while(num > (i + 1)){
        i += 1;
        factorial *= num - i;
    }
    return factorial;
}

// Ackermann Function
int ackermann(int m, int n){
    if(m == 0){
        return n + 1;
    }
    else if(m > 0 && n == 0){
        return ackermann(m-1, 1);
    }
    else if(m > 0 && n > 0){
        return ackermann(m-1, ackermann(m, n-1));
    }
    return 0;
}

// Fibonacci Function
void fibonacci(int num){
    if(num <= 0){
        cout << "{}";

    }
    else if(num == 1){
        cout << "{ 0 }";
    }
    else if(num == 2){
        cout << "{ 0, 1 }";
    }
    else{
        int values[num];
        values[0] = 0;
        values[1] = 1;
        int i = 1;
        while(i < num - 1){
            i += 1;
            values[i] = values[i - 1] + values[ i - 2];
        }
        cout << "{ ";
        for(int j = 0; j < num; j++){
            cout << values[j] << ", ";
        }
        cout << "}";
    }
}

int main()
{
//    int number;
//    cout << "Enter number to compute: ";
//    cin >> number;
//    cout << number <<"! = " << computeFactorial(number);
    fibonacci(9);
    return 0;
}
