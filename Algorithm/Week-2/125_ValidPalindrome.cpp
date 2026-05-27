#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main(){
    string s = "A man, a plan, a canal: Panama";

    // 숫자 '0' ~ '9' → 48 ~ 57
    // 대문자 'A' ~ 'Z' → 65 ~ 90
    // 소문자 'a' ~ 'z' → 97 ~ 122

    vector<char> v1;

    for(int i=0; i<s.size(); i++){
        
        if((int)s[i] >= 48 and (int)s[i] <= 57){
            v1.push_back(char((int)s[i]));

        }

        else if((int)s[i] >= 65 and (int)s[i] <= 90){
            v1.push_back(char((int)s[i] + 32));

        }

        else if((int)s[i] >= 97 and (int)s[i] <= 122){
            v1.push_back(s[i]);
        }
    }

    int  v1_size = v1.size();

    int j = 0;
    while(j != v1_size/2){
        if(v1[j] != v1[v1_size-j-1]){
            cout << "false";
            break;
        }
        j++;
    }

    if(j == v1_size/2){
        cout << "true";
    }

}


/*
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> v1;

        for (int i = 0; i < s.size(); i++) {
            if((int)s[i] >= 48 and (int)s[i] <= 57){
                v1.push_back(char((int)s[i]));
            }

            else if((int)s[i] >= 65 and (int)s[i] <= 90){
                v1.push_back(char((int)s[i] + 32));

            }

            else if((int)s[i] >= 97 and (int)s[i] <= 122){
                v1.push_back(s[i]);
            }
        }

        int v1_size = v1.size();
        int j = 0;

        while (j != v1_size / 2) {
            if (v1[j] != v1[v1_size - j - 1]) {
                return false;
            }
            j++;
        }

        return true;
    }
};




*/
