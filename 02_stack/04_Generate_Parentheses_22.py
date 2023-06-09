class Solution {
public:

    vector<string> generateParenthesis(int n) {
        return myMethod(n, "", 0);
    }

    vector<string> myMethod(int n, string solution, int closing) {
        vector<string> solutions;

        if (n == 0 && closing == 0) {
            solutions.push_back(solution);
            return solutions;
        }

        // Open or Close
        if (n > 0) {
            // Option 1: Open
            int new_closing = closing + 1;

            vector<string> recursiveSolutions = this->myMethod(n - 1, solution + "(", closing + 1);
            solutions.insert(solutions.begin(), recursiveSolutions.begin(), recursiveSolutions.end());
        }
        if (closing > 0) {
            // Option 2: Close
            vector<string> recursiveSolutions = this->myMethod(n, solution + ")", closing - 1);
            solutions.insert(solutions.begin(), recursiveSolutions.begin(), recursiveSolutions.end());
        }
        
        
        
        return vector<string>(solutions.begin(), solutions.end());

        
    }
};
