#!/bin/bash

raw_data=all_data.txt

attractions_thres=5
user_thres=5

# statistic attractions
cat $raw_data |\
    awk -F '\t' '{cnt[$2]+=1} END{for(w in cnt) {print cnt[w]"\t"w}}' |\
    sort -n -t$'\t' -k 1 -r > static_attractions.txt

# statistic users    
cat $raw_data |\
    awk -F '\t' '{cnt[$1]+=1} END{for(w in cnt) {print cnt[w]"\t"w}}' |\
    sort -n -t$'\t' -k 1 -r > static_users.txt
    
# effect attractions
cat static_attractions.txt |\
    awk -F '\t' -v thres=$attractions_thres 'BEGIN{cnt=0} {if($1 >= thres){print cnt"\t"$2; cnt += 1}}' > attraction_id.txt
    
# effect attractions
cat static_users.txt |\
    awk -F '\t' -v thres=$user_thres 'BEGIN{cnt=0} {if($1 >= thres){print cnt"\t"$2; cnt += 1}}' > user_id.txt