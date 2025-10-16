#include <iostream>
#include <string>
using namespace std;

int main() {
    // integer + if statement
    
    int a = 0;
    if (a < 0) {
        std::cout << "Integer is negative\n";
    } else if (a == 0) {
        std::cout << "Integer is zero\n";
    } else {
        std::cout << "Integer is positive\n";
    }

    // ++ and -- usage with vars

    int plusplusminusminus = 0;
    std::cout << plusplusminusminus << " " << std::endl;
    plusplusminusminus++;
    std::cout << plusplusminusminus << ' ' << std::endl;
    plusplusminusminus--;
    plusplusminusminus--;
    std::cout << plusplusminusminus << ' ' << std::endl;

    return 0;
}