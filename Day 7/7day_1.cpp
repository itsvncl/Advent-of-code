#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<string> rules;
    vector<string> bags;
    vector<string> gold;
    
    ifstream file("7day_in.txt");
    string line;
    string data;
//----------------------------------------------------------------------------------//Input and seperation
    while(getline(file, line))
    { 
        int i = 0;

        while(line[i] != ' ' || line[i+1] != 'b' || line[i+2] != 'a' || line[i+3] != 'g')
            data += line[i++];
        bags.push_back(data);
        data.clear();

        while( line[i] != '.')
            data += line[i++];
        rules.push_back(data);
        data.clear();

        if( rules.back().find("shiny gold") != string::npos )
        {
            gold.push_back(bags.back());
            rules.back() = "-";
            bags.back() = "-";
        }
    }
//----------------------------------------------------------------------------------//Part 1
    int sizeBefore = gold.size();
    bool foundAll = false;
    while(!foundAll)
    {
        foundAll = true;
        for(int i = (sizeBefore - gold.size()); i < gold.size(); i++)
        {
            for(int k = 0; k < rules.size(); k++)
            {
                if( rules.at(k).find(gold.at(i)) != string::npos )
                {
                    foundAll = false;
                    gold.push_back(bags.at(k));
                    rules.at(k) = '-';
                    bags.at(k) = '-';
                }
            }
        }
        sizeBefore += (sizeBefore - gold.size());   
    }
    
    cout << gold.size() << '\n';  
    return 0;
}