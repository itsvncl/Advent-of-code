#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

#define TREE '#'

void read_vector(vector<string> &v)
{   
    ifstream file("3day_in.txt");
    string line;
    
    while(getline(file, line))
        v.push_back(line);

    file.close();
}
int trees_hit(vector<string> map, int right, int down)
{
    int currpos = 0;
    int trees = 0;
    int width = map.at(0).length();

    for(int i = 0; i < map.size(); i += down)
    {
        if( map.at(i)[currpos] == TREE)
            trees++;
        
        currpos += right;

        if(currpos >= width)
            currpos -= width;
    }
    
    return trees;
}

int main()
{
    vector<string> map;
    read_vector(map);
                  
    cout << trees_hit(map, 3, 1) << endl
         << (long long)trees_hit(map, 1, 1) * trees_hit(map, 3, 1) * trees_hit(map, 5, 1) * trees_hit(map, 7, 1) * trees_hit(map, 1, 2) << endl;

    return 0;
}