#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main(){

    vector<int> arr = {2,4,7,8,9,10,14,15,18,23,32,50};
    int a_size = arr.size();

    int num = 0;
    int a_index = 0;
    int i = 0;
    int j = 1;
    int flag = 0;

    while(a_index < a_size){
        int fib = arr[i] + arr[j];
        for(int k=j+1; k<a_size; k++){
            if(arr[k] == fib){
                cout << arr[i] << arr[j] << fib << endl;
                i = j;
                j = k;
                num++;
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            j++;
            num = 0;
        }
        flag = 0;
        
        a_index++;
    }

    if(num == 0){
        cout << 0;
    }
    else{
        cout << num+2;
    }
}


/*
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        
        int a_size = arr.size();
        int max_num = 0;

        for(int i = 0; i < a_size - 2; i++) {
            for(int j = i + 1; j < a_size - 1; j++) {

                int p = i;
                int q = j;
                int num = 2;

                while(true) {
                    int fib = arr[p] + arr[q];
                    int flag = 0;

                    for(int k = q + 1; k < a_size; k++) {
                        if(arr[k] == fib) {
                            p = q;
                            q = k;
                            num++;
                            flag = 1;
                            break;
                        }
                        else if(arr[k] > fib) {
                            break;
                        }
                    }

                    if(flag == 0) {
                        break;
                    }
                }

                if(num >= 3) {
                    max_num = max(max_num, num);
                }
            }
        }

        return max_num;
    }
};


*/
