struct range {
    unsigned start;
    unsigned end;
};

void overlap (vector<range> ranges) {
    
    for i in range (list):
        for j in range (list):
            if ((list[i].start>=list[j].start) or (list[i].end<=list[j].end)):
                print "overlap at i[",i,"]=",list[i]," j[",j,"]=",list[j]


ranges=[]
r = range(0,0)
ranges.append(r)

for i in range (len(ranges)):
    print ranges[i],
