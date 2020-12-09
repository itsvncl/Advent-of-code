#include <bits/stdc++.h>
using namespace std;

long long find_invalid_number(vector<long long> &data)
{
    long long currentNumber;
    int currentNumberIndex;
    int j, k;
    
    for(int i = 0; i < data.size()-25 && j != currentNumberIndex; i++)
    {
        currentNumberIndex = i + 25;
        currentNumber = data.at(currentNumberIndex);
        
        j = i, k = i + 1;
        while(currentNumber != data.at(j) + data.at(k) && j != currentNumberIndex)
        {
            k++;
            if(k >= currentNumberIndex)
            {
                k = i;
                j++;
            }
        }
    }

    return currentNumber;
}
long long find_weakness_point(vector<long long> &data, long long invalidNumber) //Oh lord help the poor CPU that has to execute this abomination
{
    vector<long long> numbers;
    bool foundWeakPoint = false;
    long long sum = 0;

    int i = 0;
    while( data.at(i++) != invalidNumber && !foundWeakPoint )
    {
        int j = i;
        while( sum < invalidNumber )
        {
            numbers.push_back(data.at(j));
            sum += data.at(j++);
        }
        
        if( sum == invalidNumber )
            foundWeakPoint = true;
        else
        {
            sum = 0;
            numbers.clear();
        }
    }

    sort(numbers.begin(), numbers.end());

    return numbers.front() + numbers.back();
}
int main()
{
    ifstream file("9day_in.txt");
    vector<long long> data;
    string number;

    while(getline(file, number))
        data.push_back(stoll(number));

    long long invalidNumber = find_invalid_number(data);
    cout << invalidNumber << '\n'
         << find_weakness_point(data, invalidNumber) << '\n';

    return 0;
}