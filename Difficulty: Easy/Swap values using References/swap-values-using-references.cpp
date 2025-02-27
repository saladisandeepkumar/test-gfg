//{ Driver Code Starts
// Initial Template for C++

#include <iostream>
using namespace std;

// Function prototype
void swap(int*, int*);
void swap(int&, int&);


// } Driver Code Ends

// User function Template for C++

// Function to swap A and B
// using reference
void swap(int &a, int &b) {

    // Your code here
    int t=a;
    a=b;
    b=t;
}



//{ Driver Code Starts.

// Driver code
int main() {

    int testcase;
    cin >> testcase;

    while (testcase--) {
        int A, B;
        cin >> A >> B;

        // Swapping by reference
        swap(A, B);
        cout << A << " " << B << endl;
        cout << "~"
             << "\n";
    }

    return 0;
}
// } Driver Code Ends