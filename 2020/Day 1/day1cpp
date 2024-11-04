#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define YEAR 2020

void read_vector_from_file(vector<int> &v)
{   
    ifstream file("1day_in.txt");
    int num;
    
    while(file >> num)
        v.push_back(num);

    file.close();
}
int find_2020_sum_multy(vector<int> data)
{
    int current;

    for(int i = 0; i < data.size(); i++)
    {
        current = data.at(i);
        for(int j = i + 1; j < data.size(); j++)
        {
            if(current + data.at(j) == YEAR)
            {
                return data.at(j) * current;
            }
        }
    }
    return 0;
}
int find_2020_sum_multy_2(vector<int> data)
{
    int current;
    int current2;

    for(int i = 0; i < data.size(); i++)
    {
        current = data.at(i);
        for(int j = i + 1; j < data.size(); j++)
        {
            current2 = data.at(j);
            for(int k = i + 2; k < data.size(); k++)
            {
                if(current + current2 + data.at(k) == YEAR)
                {
                    return data.at(k) * current * current2;
                }
            }
        }
    }
    return 0;
}

int main()
{
    vector<int> data;
    read_vector_from_file(data);
    
    cout << find_2020_sum_multy(data) << endl
         << find_2020_sum_multy_2(data) << endl;

    return 0;
}
