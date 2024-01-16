#include <bits/stdc++.h>

using namespace std;

string add(string a, string b)
{
    if (a.size() < b.size())
        return add(b, a);
    if (b.size() == 0)
        return a;
    string res;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    int carry = 0, i = 0;

    while (i < b.size())
    {
        int temp1 = a[i] - '0';
        int temp2 = b[i] - '0';
        res.push_back('0' + ((temp1 + temp2 + carry) % 10));
        carry = (temp1 + temp2 + carry) / 10;
        i++;
    }
    while (carry || i < a.size())
    {
        i < a.size() ? res.push_back('0' + (((a[i] - '0') + carry) % 10)) : res.push_back('0' + (carry % 10));
        i < a.size() ? carry = ((a[i] - '0') + carry) / 10 : carry = 0;
        i++;
    }

    reverse(res.begin(), res.end());
    return res;
}

string multiply(string a, string b)
{
    if (a.size() < b.size())
        return multiply(b, a);
    string res = "0";
    int j = b.size() - 1;
    int zeros = 0;
    while (j >= 0)
    {
        string cur_res;
        int temp_b = b[j] - '0';
        int i = a.size() - 1;
        int carry = 0;
        while (i >= 0)
        {
            int temp_a = a[i] - '0';
            temp_a *= temp_b;
            temp_a += carry;
            carry = temp_a / 10;
            cur_res.push_back('0' + (temp_a % 10));
            i--;
        }
        if (carry)
            cur_res.push_back('0' + carry);
        reverse(cur_res.begin(), cur_res.end());
        for (int _ = 0; _ < zeros; _++)
            cur_res.push_back('0');
        res = add(res, cur_res);
        zeros++;
        j--;
    }
    return res;
}

string minusOne(string n)
{
    int i = n.size() - 1;
    while (i >= 0 && n[i] == '0')
    {
        n[i] = '9';
        i--;
    }
    assert(i != -1); // This can't happen!! the whole string can't be zero at this point.
    if (i == 0 && n[0] == '1')
        n = n.substr(1);
    else
        n[i] = n[i] - 1;
    return n;
}

string factorial(string n)
{
    if (n == "0" || n == "1")
        return "1";

    return multiply(n, factorial(minusOne(n)));
}

int main()
{
    string n;
    cin >> n;
    // check if input is correct
    for (char c : n)
        if (c < '0' || c > '9')
            throw invalid_argument("Input must only be a positive integer");
    // remove leading zeros
    int i = 0;
    while (i < n.size() && n[i] == '0')
        i++;
    i == n.size() ? n = "0" : n = n.substr(i);

    // For testing
    /*
    string temp = "0";
    ofstream testoutput("testoutput.txt");
    for (int _ = 0; _ <= 500; _++)
    {
        testoutput << factorial(temp);
        testoutput << "\n";
        temp = add(temp, "1");
    }
    testoutput.close();
    */

    // Output
    cout << factorial(n) << endl;

    return 0;
}
