#include <vector>
#include <tuple>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<tuple<int,int>> myStack;
        vector<int> results;

        for(unsigned int i = 1; i < temperatures.size(); i++)
        {
            while (myStack.size() > 0) {
                int stack_temp = get<1>(myStack.top());
                if (temperatures[i] > stack_temp) {
                    int old_day = get<0>(myStack.top());
                    myStack.pop();
                    results.at(old_day) = i - old_day;
                } else {
                    break;
                }
            }

            int prev_temp = temperatures[i - 1];
            if (prev_temp < temperatures[i]) {
                results.push_back(1);
            }
            else {
                results.push_back(0);
                myStack.push({i - 1, prev_temp});
            } 
           
        }
        results.push_back(0);
        return results;
    }
};
