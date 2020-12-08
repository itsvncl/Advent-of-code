#include <bits/stdc++.h>
using namespace std;

struct BagData
{
    string name;
    vector<pair<string,int>> bagsInside;
};

vector<BagData> sort_bags()
{
    ifstream file("7day_in.txt");
    string currBag, name, count;
    BagData orderedBag;
    pair<string, int> subBagData;
    vector<BagData> orderedBagData;

    while(getline(file, currBag))
    {
        int i = 0;
        while(currBag[i] != ' ' || currBag[i+1] != 'b' || currBag[i+2] != 'a' || currBag[i+3] != 'g')
            name += currBag[i++];
        orderedBag.name = name;
        name.clear();
        
        i += 13;
        if(currBag[i+1] == 'n')
        {
            subBagData.second = 0;
            subBagData.first = "No data";
            orderedBag.bagsInside.push_back(subBagData);
            orderedBagData.push_back(orderedBag);
            orderedBag = {};
            continue;
        }

        while(currBag[i] != '.')
        {
            while(currBag[i] < '0' || currBag[i] > '9') i++;

            while(currBag[i] !=' ')
                count += currBag[i++];
            subBagData.second = atoi(count.c_str());
            count.clear();
            
            i++;
            while(currBag[i] != ' ' || currBag[i+1] != 'b' || currBag[i+2] != 'a' || currBag[i+3] != 'g')
                name += currBag[i++];
            subBagData.first = name;
            name.clear();

            orderedBag.bagsInside.push_back(subBagData);

            if(currBag[i+4] == 's' && currBag[i+5] == '.' || currBag[i+4] == '.')
                break;
        }

        orderedBagData.push_back(orderedBag);
        orderedBag = {};
    }
    return orderedBagData;
}
int gold_holders(vector<BagData> bagData)
{
    vector<BagData> localData = bagData;
    vector<string> holders;
    for(int i = 0; i < localData.size(); i++)
    {
        for(int j = 0; j < localData.at(i).bagsInside.size(); j++)
        {
            if(localData.at(i).bagsInside.at(j).first == "shiny gold")
            {
                holders.push_back(localData.at(i).name);
                localData.at(i).bagsInside.clear();
            }
        }
    }

    bool foundAll = false;
    int sizeBefore = holders.size();
    while(!foundAll)
    {
        foundAll = true;
        for(int i = (sizeBefore - holders.size()); i < holders.size(); i++)
        {
            for(int j = 0; j < localData.size(); j++)
            {
                for(int k = 0; k < localData.at(j).bagsInside.size(); k++)
                {
                    if( holders.at(i) == localData.at(j).bagsInside.at(k).first )
                    {
                        foundAll = false;
                        holders.push_back(localData.at(j).name);
                        localData.at(j).bagsInside.clear();
                        
                    }
                }
            }
        }
        sizeBefore += (sizeBefore - holders.size());   
    }

    return holders.size();
}
int bag_in_bag_in_bag_in_bag_in_bag(vector<BagData> &bagData, string bagName)
{
    int ind;
    for(int i = 0; i < bagData.size(); i++)
    {
        if(bagData.at(i).name == bagName)
        {
            ind = i;
            break;
        }
    }

	int tooManyBags = 1;
	for (int i = 0; i < bagData.at(ind).bagsInside.size(); i++)
    {
        if(bagData.at(ind).bagsInside.at(i).second != 0)
		    tooManyBags += (bagData.at(ind).bagsInside.at(i).second * bag_in_bag_in_bag_in_bag_in_bag(bagData, bagData.at(ind).bagsInside.at(i).first));
	}

    return tooManyBags;
}

int main()
{
    vector<BagData> bagMap = sort_bags();
    vector<string> bagsInbag;
    cout << gold_holders(bagMap) << '\n' 
         << bag_in_bag_in_bag_in_bag_in_bag(bagMap, "shiny gold") - 1;

    return 0;
}