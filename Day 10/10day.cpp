#include <bits/stdc++.h>

int main()
{
    std::ifstream file("10day_in.txt");
    std::vector<int> data = {0}; //The first jolt
    std::string number;

    while(getline(file, number))
        data.push_back(stoi(number));

    sort(data.begin(), data.end());
    std::vector<int> jolts;

    int _1jolt = 0;
    int _3jolt = 1; // The last is always 3
    for(size_t i = 1; i < data.size(); i++)
    {
        if(data.at(i) - data.at(i-1) == 1)
            _1jolt++;
        else if(data.at(i) - data.at(i-1) == 3)
            _3jolt++;
        
        jolts.push_back(data.at(i) - data.at(i-1));
    }

    unsigned long long combinations = 1;
    int power = -1;
    for(size_t i = 0; i < jolts.size(); i++)
    {
        while(i < jolts.size() && jolts.at(i) == 1)
        {
            power++;
            i++;
        }
        if(power > 0)
        {
            int add = pow(2, power);
            if(power % 2 != 0 && power != 1) add--;  
            combinations *= add;
        }
        power = -1;
    }

    std::cout << _1jolt * _3jolt << '\n' << combinations;

    return 0;
}