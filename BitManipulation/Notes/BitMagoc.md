

# Bit manipulation

  

    Operator    Description Syntax

    &   Bitwise    AND      x & y

    |   Bitwise    OR       x | y

    ~   Bitwise    NOT        ~x

    ^   Bitwise    XOR      x ^ y

    >>  Bitwise right shift x>>

    <<  Bitwise left shift  x<<

  
  

##  let see bitwise right and left shift operator in details

  

## left shift operator

   - x=3  x<<1  here we are doing left shift of x by 1 bit

   - in binary rep of 32 bit system 3=  0000000....0011  

   ### now we are left shifting by 1

    31 bit move a place ahed and leading bit i.e 0 will be get ingnored and 0 will be appended in lsb

    3<<1-00000.....00110=6 in decimal

    x<<2:00000.....001100 =12

    x<<y \=x\*2^y.. irrespective x is postive or negative

## Applications of Left Shift Operator

    1.Multiplication by Powers of Two: Left shifting a number by n positions is equivalent to multiplying it by 2^n and is much faster than normal multiplication

    2.Efficient Calculations: Used in performance-critical applications where arithmetic operations need to be fast.

    3.Bit Manipulation: Common in low-level programming, such as embedded systems and hardware interfacing.



## Right shift operator 
   - singed right shift operator :it takes care of signed bit 
    if number is postive it will make sure it will postive and same for negative numbr

   - it is just opposite of left shift ...trailing bits will be ignored 
    x>>y= x/2^y

    Applications of Right Shift Operators
    1 .Division by Powers of Two: Right shifting a number by n positions is equivalent to dividing it by 2^n and it is very fast.

    2.Efficient Calculations: Used in performance-critical applications for fast division operations.

    3.Bit Manipulation: Useful in extracting specific bits from data, common in data compression and cryptography.


## XOR Operator    
     The result in each position is 1 if only one of the two bits is 1 but will be 0 if both are 0 or both are 1.

The truth table for the XOR (exclusive OR) operation is as follows:

| A | B  | A XOR B |
|---|--- |---------|
| 0 | 0  |    0    |
| 0 | 1  |    1    |   
| 1 | 1  |    0    |   
| 1 | 0  |    1    |


```python
a = 10  # 1010 in binary
b = 6   # 0110 in binary

result = a ^ b  # 1100 in binary

print(result)  # Output: 12

```
## Use Cases of Bitwise XOR Operator:
  - Flipping individual bits:

        The XOR operator can be used to flip individual bits in a number.
        For example, x ^ 1 will flip the least significant bit of x.


   - Swapping two variables without a temporary variable

         The XOR operator can be used to swap the values of two variables without using a temporary variable. 
         For example, a ^= b; b ^= a; a ^= b; will swap the values of a and b.

     ```python
         def swapTwo(a,b):
            a^=b
            b^=a
- Checking if two numbers have opposite signs: 

    
       The XOR operator can be used to check if two numbers have opposite signs. 
       For example
      (x ^ y) < 0 will return true if x and y have opposite signs.

   ```python
      def checkSign(a,b):
         if a^b<0:
            return True
         else:
            return False

      a=-1
      b=2
      print(checkSign(a,b))  
 - Detecting changes in data: 

       The XOR operator can be used to detect changes in data. For example, 
       x ^ y will return 0 if x and y are the same, and a non-zero value if they are different. 

       a^a=0
       0^a=a     