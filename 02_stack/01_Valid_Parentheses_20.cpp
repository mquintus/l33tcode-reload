#include <iostream>
#include <algorithm>

class Solution {
public:
    map<string, char> complement;

    Solution() {
        this->complement[")"] = '(';
        this->complement["}"] = '{';
        this->complement["]"] = '[';
    }

    bool isValid(string s) {
        //std::cout << s << "\n";
        if (s.size() % 2 == 1)
            return false;

        for (int i = 0; i < s.size(); i++) {
            map<string,char>::iterator it = this->complement.find(s.substr(i, 1));
            if (it != this->complement.end()) {
                // closing bracket was found
                if (i == 0) 
                    return false; // closing bracket was first char

                if (it->second == s[i - 1]) {
                    s = s.substr(0, i - 1) + s.substr(i + 1);
                    i = i - 2;
                    //std::cout << s << "\n";
                }
            }
        }

        if (s.size() == 0)
            return true;

        return false;
    }
};
